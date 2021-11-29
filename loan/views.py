import re
from django.db.models.fields import BooleanField
from django.db.models.fields.related import RECURSIVE_RELATIONSHIP_CONSTANT
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from datetime import datetime

from account.models import User
from .models import (
    InvestorFullFilmentProposal,
    LoanProposal,
    BorrowerAssets,
    EmploymentDetails
)

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.core.mail import EmailMessage



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
        approved =  InvestorFullFilmentProposal.objects.all()
        

        context = {
            'all_loans' :  loan_proposal,
            'borrower' :  assets,
            'approved' :approved
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
    approved = InvestorFullFilmentProposal.objects.all()

    context = {
        'all_loans' : all_loanns,
        'approved' :  approved
    }
    return render(request,'applied_loans.html',context)

@login_required(login_url="account:sign_in")
def view_loan_applicants(request,pk):
    loan =  LoanProposal.objects.get(id =  pk)
    borrower =  BorrowerAssets.objects.all()

    context = {
        'loan': loan,
        'borrower' :  borrower
    }

    return render(request,'view_all_applicants.html',context)


@login_required(login_url="account:sign_in")
def validate_user_loan(request,pk):
    loan =  LoanProposal.objects.get(id =  pk)

    borrower =  BorrowerAssets.objects.get(loan_proposal = loan)
    employment_details = EmploymentDetails.objects.get(loan_proposal =  loan)


    context = {
        'loan': loan,
        'borrower': borrower,
        'employment_details':employment_details
    }

    if request.method ==  "POST":
        approve = request.POST.get("approve")
        release_date_from_investor =  request.POST.get("release_date_from_investor")
      
        disburd_date_to_borrower =  request.POST.get("disburd_date_to_borrower")
        if approve == "on":
            print(datetime.strptime(release_date_from_investor, '%Y-%m-%d'),"hgfdsdfghjk")
            obj,created = InvestorFullFilmentProposal.objects.get_or_create(investor_proposal_id = loan,farmer_id = borrower.user_id)
            obj.release_date_from_investor = release_date_from_investor
            obj.disburd_date_to_borrower =  disburd_date_to_borrower
            obj.accepted_declied =  True
            obj.save()
            current_site = get_current_site(request)
            email_subject = 'Loan Approval'
            user = borrower.user_id
            message = render_to_string('loan_success.html', {
            'user': user,
            'domain': current_site.domain,
            
            
            })
            to_email = borrower.user_id.email
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()

            return redirect("/")




    return render(request,'validate_user_loan.html',context)



