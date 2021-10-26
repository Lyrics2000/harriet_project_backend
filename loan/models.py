from re import M
from typing import Match
from django.db import models
from django.db.models.fields import BooleanField
from authentification.models import User
from mainapp.models import BaseModel


# Create your models here.
class BorrowerExtraInfo(BaseModel):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    current_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField()
    highest_level_of_education = models.CharField(max_length=255)

    def __str__(self):
        return self.current_address

class BorrowerAssets(BaseModel):
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    asset_type = models.CharField(max_length=255)
    asset_value = models.DecimalField(max_digits=20,decimal_places=2)
    ownership_percentage = models.DecimalField(max_digits=20,decimal_places=2)
    possession_since = models.DateTimeField()

    def __str__(self):
        return self.asset_type
 
class EmploymentDetails(BaseModel):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    employment_type = models.CharField(max_length=255) # fulltime /partime
    profession_type = models.CharField(max_length=255)
    employment_description = models.TextField()
    salary_range = models.CharField(max_length=255)

    def __str__(self):
        return self.employment_type


class LoanProposal(BaseModel):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    proposal_amount = models.DecimalField(max_digits=20,decimal_places=2)
    cancel_date = models.DateTimeField()
    publish = BooleanField(default=False)

    def __str__(self):
        return str(self.user_id)


class LoanTicket(BaseModel):
    borrower_id = models.ForeignKey(User,on_delete=models.CASCADE)
    loan_proposal_id =  models.ForeignKey(LoanProposal,on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=20,decimal_places=2)
    loan_tenure_in_months = models.IntegerField()
    interest_rate = models.DecimalField(max_digits=20,decimal_places=2)
    reason_for_loan =  models.TextField()


    def __str__(self):
        return str(self.borrower_id)

class InvestorFullFilmentProposal(BaseModel):
    investor_proposal_id = models.ForeignKey(LoanProposal,on_delete=models.CASCADE,null=True,blank=True)
    loan_ticket_id = models.ForeignKey(LoanTicket,on_delete=models.CASCADE,blank=True,null=True)
    release_date_from_investor = models.DateTimeField()
    disburd_date_to_borrower = models.DateTimeField()
    accepted_declied =  models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.investor_id)
 



