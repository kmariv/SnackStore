from .models import * 
from rest_framework import serializers
from django.contrib.auth.hashers import *
from django.contrib.auth.models import User as AUTH_USER

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
	
	def create(self, validated_data):
		copy_validated_data = validated_data

		if 'password' in validated_data.keys():
			copy_validated_data['password'] = make_password(str(validated_data['password']), salt=None, hasher='sha1')
		
		AUTH_USER.objects.create(	username=validated_data['username'],
	                            	email = '',
	                            	password=copy_validated_data['password']
								)

		return User(**copy_validated_data)
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