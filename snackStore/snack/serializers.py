from .models import * 
from rest_framework import serializers

class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = ('snack_id','name','is_active','stock_quantity','price')