from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.http import StreamingHttpResponse
from django.views.static import serve

import subprocess
import os
import math
import threading
import time
import pdb
from .models import Company,Nation,Bank,Transfers,ComRelation,ProdTrans,ComBank,Material,ProdReq,BankNation,LoanTrans,ComMat


# Create your views here.
def index(request):	

	return HttpResponse("Add data throguh admin page and then call visit /net/relate to populate the related db")

def Relate(request):
	companies = Company.objects.all().order_by("pk")
	nations = Nation.objects.all().order_by("pk")
	banks = Bank.objects.all().order_by("pk")
	materials = Material.objects.all().order_by("pk")
	for n in nations:
		for b in banks:
			bn = BankNation(nation=n,bank=b,veto_part=0)
			bn.save()

	for c in companies:
		for m in materials:
			cm = ComMat(com=c,mat=m,amt=100)
			cm.save()
	return HttpResponse("Hello Wrold")

def tp(request):
	context={}
	return render(request,'netIITD/tp.html',context)

def showall(request):
	companies = Company.objects.all().order_by("pk")
	commats = ComMat.objects.all().order_by("com_id","mat_id")			# to represent amt of material each company has
	nations = Nation.objects.all().order_by("pk")
	banks = Bank.objects.all().order_by("pk")
	materials = Material.objects.all().order_by("pk")
	banknations = BankNation.objects.all().order_by("nation_id","bank_id")	# to represent veto power of each bank a nation has
	template = loader.get_template('netIITD/index.html')
	context = { 'companies':companies, 'nations':nations,'banks':banks, 'materials':materials,'banknations':banknations,'bankNo':range(1,len(banks)+1), 'commats':commats}
	return render(request,'netIITD/index.html',context)

def addComTrans(request):
	subsidy=2.2
	try:
		#pdb.set_trace()
		c1=Company.objects.get(pk=request.POST['c1'])
		c2=Company.objects.get(pk=request.POST['c2'])
		mat_id=int(request.POST['mat'])
		mat=Material.objects.get(pk=mat_id)
		units=int(request.POST['units'])
		ppu=int(request.POST['ppu'])
		moneyEx = ppu*units
		c1Mat = ComMat.objects.get(com=c1,mat=mat)
		c2Mat = ComMat.objects.get(com=c2,mat=mat)
		if(c1.id==c2.id or ppu<0 or units<0 or c1Mat.amt<units or c2.com_money< moneyEx):
			return HttpResponse("Inputs don't make sense! Go back and change things properly.")
	except (KeyError, Company.DoesNotExist):
		return render(request,'netIITD/index.html',{'error_message':'Selected Choice does not exist',})
	else:
		c1Mat.amt = c1Mat.amt - units
		c2.com_money = c2.com_money -  moneyEx
		tmpid = c2.com_type.id
		if(c1.com_type.id==mat_id and ((tmpid-1)%7== (mat_id)%7 or (tmpid-2)%7== mat_id%7 or (tmpid-3)%7== mat_id%7)):
			moneyEx = moneyEx*subsidy
		c1.com_money = c1.com_money + moneyEx
		c2Mat.amt = c2Mat.amt + units
		pt = ProdTrans(com1=c1,com2=c2,prod_type=mat,price_per_unit=ppu,prod_units=units)
		pt.save()
		c1.save()
		c2.save()
		c1Mat.save()
		c2Mat.save()
	return redirect('/net/showall')

def prodDone(com,mat,quan,prod,t1):
	time.sleep(12)
	factor = 2
	m = ComMat.objects.get(com=com,mat=mat)
	m.amt = m.amt+quan*factor
	m.save()
	com.prod_units = com.prod_units+prod
	com.save()

def addProdReq(request):
	capacity=2
	try:
		com = Company.objects.get(pk=request.POST['com'])
		mat = Material.objects.get(pk=com.com_type.id)
		mat1 = Material.objects.get(pk=request.POST['mat1'])
		mat2 = Material.objects.get(pk=request.POST['mat2'])
	#	pdb.set_trace()
		noMat = len(Material.objects.all())
		quantity = int(request.POST['quantity'])
		if((mat.id-1)%noMat!= (mat1.id%noMat) and (mat.id-2)%noMat!= (mat1.id%noMat) and (mat.id-3)%noMat!= (mat1.id%noMat) ):
			return HttpResponse("Material 1 input cannot be used to produce output.")
		if((mat.id-1)%noMat != (mat2.id%noMat) and (mat.id-2)%noMat != (mat2.id%noMat) and (mat.id-3)%noMat!= (mat2.id%noMat) ):
			return HttpResponse("Material 2 input cannot be used to produce output.")
		if(mat1.id==mat2.id):
			return HttpResponse("You entered the same material twice")
		m1 = ComMat.objects.get(com=com,mat=mat1) 
		m2 = ComMat.objects.get(com=com,mat=mat2) 
		if(m1.amt<quantity or m2.amt<quantity or quantity > com.prod_units*capacity):
			return HttpResponse("You do not have so many raw materials")
	except (KeyError, Company.DoesNotExist):
		return render(request,'netIITD/index.html',{'error_message':'Selected Choice non-existent',})
	else:
		#reduce mat1,mat2,produnits
		m1.amt = m1.amt - quantity
		m2.amt = m2.amt - quantity
		useProd = math.ceil(quantity/capacity)
		com.prod_units = com.prod_units - useProd
		com.save()
		m1.save()
		m2.save()
		pr = ProdReq(com=com,out=mat,prod_units = useProd)
		pr.save()
		t = threading.Thread(target=prodDone,args=(com,mat,quantity,useProd,time.time()))
		t.start()
		return redirect('/net/showall')

def purProdHouse(request):
	nat = Nation.objects.get(pk=request.POST['nat'])
	com = Company.objects.get(pk=request.POST['com'])
	ppph = int(request.POST['ppph'])
	numProd = int(request.POST['prodh'])

	if(numProd>nat.prod_units or ppph*numProd>com.com_money):
		return Http.Response("Either not enough Prod units with the nation or not enough money with the company")
	
	nat.nation_money = nat.nation_money + ppph*numProd
	com.com_money = com.com_money - ppph*numProd
	nat.prod_units = nat.prod_units - numProd
	com.prod_units = com.prod_units + numProd

	com.save()
	nat.save()

	return redirect('/net/showall')

def purBankVeto(request):
	nat = Nation.objects.get(pk=request.POST['nat'])
	bank = Bank.objects.get(pk=request.POST['bank'])
	price = int(request.POST['price'])
	vetoDemand = int(request.POST['veto_demand'])
	bn = BankNation.objects.get(nation=nat,bank=bank)

	if(vetoDemand>bank.veto or price>nat.nation_money):
		return Http.Response("Either not enough  Veto with the bank or not enough money with the nation")
	
	nat.nation_money = nat.nation_money - price
	bank.bank_money = bank.bank_money + price
	bank.veto = bank.veto - vetoDemand
	bn.veto_part = bn.veto_part + vetoDemand
	bn.save()
	bank.save()
	nat.save()
	return redirect('/net/showall')

def BankLoan(request):
	com = Company.objects.get(pk=request.POST['com'])
	bank = Bank.objects.get(pk=request.POST['bank'])
	loan = int(request.POST['loanamt'])
	interest = float(request.POST['interest'])
	interest = interest/100
	com.com_money = com.com_money + loan
	bank.bank_money = bank.bank_money - loan
	l = LoanTrans(com=com,bank=bank,ret=loan*(1+interest))
	com.save()
	bank.save()
	l.save()
	return redirect('/net/showall')

def Payback(request):
	loans = LoanTrans.objects.all()
	for l in loans:
		com = l.com
		bank = l.bank
		ret = l.ret
		if(com.com_money<ret):
			ret = com.com_money
		com.com_money = com.com_money-ret
		bank.bank_money = bank.bank_money + ret
		com.save()
		bank.save()
	return redirect('/net/showall')

def RetGov(request):
	coms = Company.objects.all()
	for c in coms:
		mat = c.com_type
		matq = ComMat.objects.get(com=c,mat=mat)
		c.com_money = c.com_money + matq.amt * mat.base_price
		matq.amt=0
		c.save()
		matq.save()
	return redirect('/net/showall')

#@csrf_exempt
def SaveData(request):
	dbname = request.POST['dbname']
	dbname = "save_"+dbname
	cmd = "./backup.sh "+dbname
	os.system(cmd)
	di = os.getcwd()
	f = open("../"+dbname)
	outp = f.read()
	f.close()

	return serve(request, os.path.basename(dbname), os.path.dirname(dbname))
	#response = StreamingHttpResponse(outp)
	#response['Content-Type'] = 'text/plain; charset=utf8'
	#return response

def Restart(request):
	companies = Company.objects.all()
	return HttpResponse("Hey buddy")


def Reset(request):
	cmd = "./reset.sh"
	os.system(cmd)
	return redirect('/net/showall')

