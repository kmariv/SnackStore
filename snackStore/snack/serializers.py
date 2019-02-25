from .models import * 
from rest_framework import serializers
from django.contrib.auth.hashers import *

from django.forms.models import model_to_dict

class SnackSerializer(serializers.HyperlinkedModelSerializer):
	def validate(self,data):
		if 'name' not in data.keys()== 0:
			raise serializers.ValidationError("The snack should have a name")
		return data

	class Meta:
		model = Snack
		fields = ('snack_id','name','stock_quantity','price','popularity')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	def update(self, instance, data):
		if 'password' in data.keys():
			instance.password = make_password(str(data['password']), salt=None, hasher='sha1')
		instance.save()
		return instance

	class Meta:
		model = User 
		fields = ('user_id','username','name','last_name','is_admin','is_active','password')



class PurchaseSerializer(serializers.ModelSerializer):
	user = serializers.StringRelatedField(many=False)#many=True, view_name='user-detail')
	
	snack = serializers.StringRelatedField(many=False)#many=True, view_name='snack-detail')

	class Meta:
		model= Purchase
		fields = ('user','snack','quantity')


class SnackPopularitySerializer(serializers.ModelSerializer):
	user 	= serializers.StringRelatedField(many=False)
	snack 	= serializers.StringRelatedField(many=False)

	class Meta:
		model = SnackPopularity
		fields = ('user','snack','action_date')

class SnackPriceLogSerializer(serializers.ModelSerializer):
	user 	= serializers.StringRelatedField(many=False)
	snack 	= serializers.StringRelatedField(many=False)

	class Meta:
		model = SnackPriceLog
		fields = ('user','snack','action_date','old_price','new_price')