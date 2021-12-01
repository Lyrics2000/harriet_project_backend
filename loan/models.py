from re import M
from typing import Match
from django.db import models
from django.db.models.fields import BooleanField
from account.models import User
from mainapp.models import BaseModel, upload_image_path
from django.shortcuts import reverse


# Create your models here.
class BorrowerExtraInfo(BaseModel):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    current_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField()
    highest_level_of_education = models.CharField(max_length=255)

    def __str__(self):
        return self.current_address


class LoanProposal(BaseModel):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    loan_title  =  models.CharField(max_length=255,blank=True,null=True)
    proposal_amount = models.DecimalField(max_digits=20,decimal_places=2)
    loan_details =  models.TextField(blank=True,null=True)
    publish = BooleanField(default=False)
    

    def __str__(self):
        return str(self.user_id)

    def get_absolute_url(self):
        return reverse("loan:edit_loan", kwargs={
            'pk': self.id
        })

    def get_apply_loan(self):
        return reverse("loan:apply_loan", kwargs={
            'pk': self.id
        })

    def view_loan_applicants(self):
        return reverse("loan:all_loan_applicants", kwargs={
            'pk': self.id
        })

    def validate_user_loan_applicants(self):
        return reverse("loan:validate_user_loan", kwargs={
            'pk': self.id
        })

    



class BorrowerAssets(BaseModel):
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    loan_proposal =  models.ForeignKey(LoanProposal,on_delete=models.CASCADE,blank=True,null=True)
    statement_statement =  models.FileField(upload_to=upload_image_path,blank=True,null=True)
    

    def __str__(self):
        return str(self.user_id)
 
class EmploymentDetails(BaseModel):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    loan_proposal =  models.ForeignKey(LoanProposal,on_delete=models.CASCADE,blank=True,null=True)
    employment_type = models.CharField(max_length=255) # fulltime /partime
    profession_type = models.CharField(max_length=255)
    employment_description = models.TextField()
    salary_range = models.CharField(max_length=255)

    def __str__(self):
        return self.employment_type










class InvestorFullFilmentProposal(BaseModel):
    investor_proposal_id = models.ForeignKey(LoanProposal,on_delete=models.CASCADE,null=True,blank=True)
    farmer_id = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    release_date_from_investor = models.CharField(max_length=255,blank=True,null=True)
    disburd_date_to_borrower = models.CharField(max_length=255,blank=True,null=True)
    accepted_declied =  models.BooleanField(default=False)

    def __str__(self):
        return str(self.investor_proposal_id)
 



