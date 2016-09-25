from django.db import models

# Create your models here.

class Material(models.Model):
	material_name = models.CharField(max_length=50)
	base_price = models.FloatField(default=1000)
	def __str__(self):
		return self.material_name

class Company(models.Model):
	com_name = models.CharField(max_length=50)
	com_type = models.ForeignKey(Material,on_delete=models.CASCADE)
	com_money = models.FloatField(default=20000.0)
	prod_units = models.IntegerField(default=0)
	
	def __str__(self):
		return self.com_name

class ComMat(models.Model):
	com = models.ForeignKey(Company)
	mat = models.ForeignKey(Material)
	amt = models.FloatField(default=10)

	def __str__(self):
		return (self.com.com_name + " -> " + self.mat.material_name)

class Nation(models.Model):
	nation_name = models.CharField(max_length=50)
	nation_money = models.FloatField(default=100000)
	prod_units = models.IntegerField(default=3)

	def __str__(self):
		return self.nation_name

class Bank(models.Model):
	bank_name = models.CharField(max_length=50)
	bank_money = models.FloatField(default=600000)
	veto = models.FloatField(default=100)
	
	def __str__(self):
		return self.bank_name

class BankNation(models.Model):
	nation = models.ForeignKey(Nation)
	bank = models.ForeignKey(Bank)
	veto_part = models.FloatField(default=0)

	def __str__(self):
		return (self.nation.nation_name+" - "+self.bank.bank_name)

class LoanTrans(models.Model):
	com = models.ForeignKey(Company)
	bank = models.ForeignKey(Bank)
	ret = models.FloatField(default=0)
	
	def __str__(self):
		return (self.bank.bank_name+" - "+self.com.com_name)	


class ProdReq(models.Model):
	com = models.ForeignKey(Company)
	out = models.ForeignKey(Material)
	prod_units = models.IntegerField()
	tim = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.com.com_name+" -> "+self.out.material_name


class ProdTrans(models.Model):
	com1 = models.ForeignKey(Company,related_name='c1')
	com2 = models.ForeignKey(Company,related_name='c2')
	prod_type = models.ForeignKey(Material,on_delete=models.CASCADE)
	price_per_unit = models.FloatField(default=1)
	prod_units = models.IntegerField()

	def __str__(self):
		return self.com1.com_name+" - "+self.com2.com_name+" : "+self.prod_type.material_name

class PurProdHouse(models.Model):
	com = models.ForeignKey(Company)
	nation = models.ForeignKey(Nation)
	prod_units = models.IntegerField()

	def __str__(self):
		return self.com.com_name+" - "+self.nation.nation_name+" : "+self.prod_units

class PurBankVeto(models.Model):
	nation = models.ForeignKey(Nation)
	bank = models.ForeignKey(Bank)
	veto = models.FloatField()
	price = models.FloatField()


