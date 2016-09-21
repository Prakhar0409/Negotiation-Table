from django.conf.urls import url
from . import views

app_name='netIITD'
urlpatterns = [
	url(r'^$',views.index),	
	url(r'showall',views.showall),
	url(r'tp',views.tp),
	url(r'comtrans',views.addComTrans,name='comtrans'),
	url(r'prodreq',views.addProdReq,name='prodreq'),
	url(r'prodhpur',views.purProdHouse,name='prodhpur'),
	url(r'purbankveto',views.purBankVeto,name='purbankveto'),
	url(r'bankloan',views.BankLoan,name='bankloan'),
	url(r'payback',views.Payback,name='payback'),
	url(r'retgov',views.RetGov,name='retgov'),
	url(r'savedata',views.SaveData,name='savedata'),
	url(r'reset',views.Reset,name='reset'),
	url(r'relate',views.Relate,name='relate'),
	url(r'restart',views.Restart,name='restart'),
]
