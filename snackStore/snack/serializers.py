from .models import * 
from rest_framework import serializers

class SnackSerializer(serializers.HyperlinkedModelSerializer):
	def validate(self,data):
		if 'name' not in data.keys()== 0:
			raise serializers.ValidationError("The snack should have a name")
		return data

	class Meta:
		model = Snack
		fields = ('snack_id','name','is_active','stock_quantity','price','popularity')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User 
		fields = ('username','name','last_name','is_admin','is_active')


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