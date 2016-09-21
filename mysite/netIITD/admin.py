from django.contrib import admin

from .models import Company,Nation,Bank,Transfers,ComRelation,ProdTrans,ComBank,Material,ProdReq,BankNation,LoanTrans,ComMat
# Register your models here.

admin.site.register(Material)
admin.site.register(Company)
admin.site.register(Nation)
admin.site.register(Bank)
admin.site.register(ComRelation)
admin.site.register(ProdTrans)
admin.site.register(ComBank)
admin.site.register(Transfers)
admin.site.register(ProdReq)
admin.site.register(BankNation)
admin.site.register(LoanTrans)
admin.site.register(ComMat)
