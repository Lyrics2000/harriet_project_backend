

from os import name
from django.urls import path
from .views import (
    delete_loan,
    upload_loan,
    loans,
    loan_details,
    delete_loan,
    edit_loan,
    apply_loan,
    applied_loans
   
)

app_name = "loan"
urlpatterns = [
    path('',upload_loan,name="upload_loan"),
    path('loans/',loans,name="loans"),
    path('loan_details/',loan_details,name="loan_details"),
    path('delete_loan/',delete_loan,name="delete_loan"),
    path('edit_loan/<pk>/',edit_loan,name="edit_loan"),
    path('apply_loan/<pk>/',apply_loan,name="apply_loan"),
    path('applied_loans/',applied_loans,name="applied_loans")


]
