from django.contrib import admin
from .models import (
    BorrowerExtraInfo,
    BorrowerAssets,
    EmploymentDetails,
    LoanProposal,
    LoanTicket,
    InvestorFullFilmentProposal
)

# Register your models here.
admin.site.register(BorrowerExtraInfo)
admin.site.register(BorrowerAssets)
admin.site.register(EmploymentDetails)
admin.site.register(LoanProposal)
admin.site.register(LoanTicket)
admin.site.register(InvestorFullFilmentProposal)
