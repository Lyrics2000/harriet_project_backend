from django.db.models.fields import BooleanField
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from account.models import User
from .models import (
    LoanProposal,
    BorrowerAssets,
    EmploymentDetails
)



# Create your views here.

@login_required(login_url="account:sign_in")
def upload_loan(request):
    if request.method == "POST":
        user =  request.user
        user_id =  request.user.id
        loan_title =  request.POST.get("loan_title")
        loan_amount =  request.POST.get("loan_amount")
        loan_requirements =  request.POST.get("loan_requirements")
        user_obj =  User.objects.get(id =  user_id)
        LoanProposal.objects.create(
            user_id =  user_obj,
            loan_title = loan_title,
            proposal_amount =  float(loan_amount),
            loan_details =  loan_requirements,
            publish =  True
        )

        return redirect("loan:upload_loan")

    return render(request,'upload_loan.html')


@login_required(login_url="account:sign_in")
def loans(request):
    loan_proposal =  LoanProposal.objects.all()
    user_id =  request.user.id
    user_obj =  User.objects.get(id =  user_id)
    farmer = user_obj.type
    
    if farmer  == "Farmer":
        assets =  BorrowerAssets.objects.filter(user_id  =  user_obj)

        context = {
            'all_loans' :  loan_proposal,
            'borrower' :  assets
        }
        return render(request,'loans.html',context)

    context = {
            'all_loans' :  loan_proposal,
            'borrower' :  False
        }
    return render(request,'loans.html',context)
    

@login_required(login_url="account:sign_in")
def loan_details(request):
    if request.method == "POST":
        loan_id =  request.POST.get("loan_id")
        loan_obj =  LoanProposal.objects.get(id =  loan_id)
        context = {
            'loan': loan_obj
        }
        return render(request,'loan_details.html',context)
    return render(request,'loan_details.html')


@login_required(login_url="account:sign_in")
def delete_loan(request):
    if request.method == "POST":
        loan_id =  request.POST.get("loan_id")
        LoanProposal.objects.get(id =  loan_id).delete()
        return redirect("loan:loans")


@login_required(login_url="account:sign_in")
def edit_loan(request,pk):
    loan_obj = LoanProposal.objects.get(id =  pk)
    context = {
        'loan':loan_obj
    }
    if request.method == "POST":
      
        title = request.POST.get("title")
        amount =  request.POST.get("amount")
        loan_requirements =  request.POST.get("loan_requirements")
        loan_obj.loan_title = title
        loan_obj.proposal_amount =  amount
        loan_obj.loan_details =  loan_requirements
        loan_obj.save()

        return redirect("loan:loans")

 
    return render(request,'loan_edit.html',context)

@login_required(login_url="account:sign_in")
def apply_loan(request,pk):
    loan_obj = LoanProposal.objects.get(id =  pk)
    user_id =  request.user.id
    user_obj =  User.objects.get(id =  user_id)
    context = {
        'loan':loan_obj
    }
    if request.method == "POST":
        employment_type =  request.POST.get("employment_type")
        employment_industry =  request.POST.get("employment_industry")
        employment_description =  request.POST.get("employment_description")
        salary_range =  request.POST.get("salary_range")
        statement =  request.FILES['statement']
        BorrowerAssets.objects.create(
            user_id = user_obj,
            loan_proposal =  loan_obj,
            statement_statement =  statement

        )

        request.session['loan_proposal_id'] = loan_obj.id
        

        
        EmploymentDetails.objects.create(
            user_id =  user_obj,
            loan_proposal =  loan_obj,
            employment_type =  employment_type,
            profession_type =  employment_industry,
            employment_description = employment_description,
            salary_range = salary_range

        )

        return redirect("loan:loans")

    return render(request,'apply_loan.html',context)


@login_required(login_url="account:sign_in")
def applied_loans(request):
    user_id =  request.user.id
    user_obj =  User.objects.get(id =  user_id)
    all_loanns =  BorrowerAssets.objects.filter(user_id =  user_obj)

    context = {
        'all_loans' : all_loanns
    }
    return render(request,'applied_loans.html',context)



