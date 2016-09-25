from django.contrib import admin

from .models import Company,Nation,Bank,ProdTrans,Material,ProdReq,BankNation,LoanTrans,ComMat,PurProdHouse,PurBankVeto
# Register your models here.

admin.site.register(Material)
admin.site.register(Company)
admin.site.register(Nation)
admin.site.register(Bank)
admin.site.register(ProdTrans)
admin.site.register(ProdReq)
admin.site.register(BankNation)
admin.site.register(LoanTrans)
admin.site.register(ComMat)
admin.site.register(PurProdHouse)
admin.site.register(PurBankVeto)
