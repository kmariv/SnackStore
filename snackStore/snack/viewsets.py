# -*- coding: utf-8 -*-
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

#from django_filters import rest_framework as filters
from rest_framework import filters as f

# class SnackFilter(filters.FilterSet):
# 	class Meta:
# 		model = Snack
# 		fields = {
# 					'name' : ['icontains'],
# 					'stock_quantity': ['gte','gt']
# 				}

class SnackViewSet(viewsets.ModelViewSet):
	#queryset = Snack.objects.all()
	serializer_class = SnackSerializer
	#filterset_class = SnackFilter
	filter_backends = (f.SearchFilter, f.OrderingFilter)
	filterset_fields = ('name', 'stock_quantity',)
	ordering_fields = ('name','popularity','price',)
	search_fields = ('name',)

	def get_queryset(self):
		return Snack.objects.all()

	# @action(methods=['get'],detail=False)
	# def sort_by_name(self, request):
	# 	qs = self.get_queryset().order_by('name')
	# 	serializer = self.get_serializer_class()(qs)
	# 	return Response(serializer.data)