# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Snack(models.Model):
	snack_id 		= models.AutoField(primary_key=True)
	name 			= models.CharField('Name',max_length=50,default='')
	#is_active 		= models.BooleanField('Is active', default=True) 
	stock_quantity 	= models.PositiveSmallIntegerField('Snack', default=0)
	price 			= models.DecimalField('Price', max_digits=5, decimal_places=2, default=0.0)
	popularity 		= models.PositiveSmallIntegerField('Popularity', default=0)

	def __unicode__(self):
		return self.name

class User(models.Model):
	user_id 		= models.AutoField(primary_key=True)
	username 		= models.CharField('Username',max_length=50,unique=True)
	name 			= models.CharField('Name',max_length=50,default='')
	last_name 		= models.CharField('Last name',max_length=50)
	is_admin 		= models.BooleanField('Is admin', default=False)
	is_active 		= models.BooleanField('Is active', default=True) 

	def __unicode__(self):
		return self.username

class Purchase(models.Model):
	purchase_id 	= models.AutoField(primary_key=True)
	user 			= models.ForeignKey('User',related_name='User_Purchase',verbose_name='User') 
	snack 			= models.ForeignKey('Snack',related_name='Snack_Purchase',verbose_name='Snack')
	quantity 		= models.PositiveSmallIntegerField('Quantity', default=0) 
	action_date 	= models.DateTimeField('Action date', auto_now_add=True) 

class SnackPopularity(models.Model):
	snack_popularity_id = models.AutoField(primary_key=True)
	user 			= models.ForeignKey('User',related_name='User_SnackPopularity',verbose_name='User') 
	snack 			= models.ForeignKey('Snack',related_name='Snack_SnackPopularity',verbose_name='Snack')
	action_date 	= models.DateTimeField('Action date', auto_now_add=True) 

class SnackPriceLog(models.Model):
	snack_price_log_id 	= models.AutoField(primary_key=True)
	user 				= models.ForeignKey('User',related_name='User_SnackPriceLog',verbose_name='User') 
	snack 				= models.ForeignKey('Snack',related_name='Snack_SnackPriceLog',verbose_name='Snack')
	old_price 			= models.DecimalField('Old Price', max_digits=5, decimal_places=2, default=0.0)
	new_price 			= models.DecimalField('New Price', max_digits=5, decimal_places=2, default=0.0)
	action_date 		= models.DateTimeField('Action date', auto_now_add=True) 