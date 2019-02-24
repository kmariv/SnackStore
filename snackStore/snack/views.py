# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def snack_list(request,format = None):
	if request.method == 'GET':
		snack = Snack.objects.all()
		serializer = SnackSerializer(snack, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = SnackSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snack_detail(request, pk,format = None):
	try:
		snack = Snack.objects.get(pk=pk)
	except Snack.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = SnackSerializer(snack)
		return Response(serializer.data)

	elif request.method == 'PUT':	
		try: 
			user = User.objects.get(username= request.data['username'])
		except User.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = SnackSerializer(snack, data=request.data)
		if serializer.is_valid():
			print snack.price
			print request.data['price']
			if snack.price != request.data['price']:
				SnackPriceLog.objects.create(
											user= 	 		user	
											,snack= 		snack
											,old_price= 	snack.price
											,new_price= 	request.data['price']
											)
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		snack.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def like_product(request, snack_id, user_id, format=None):
	try:
		snack = Snack.objects.get(pk=snack_id)
	except Snack.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	try: 
		user = User.objects.get(pk= user_id)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'POST':
		snack.popularity = snack.popularity + 1
		snack.save()

		popularity = SnackPopularity.objects.create(
														user 	= user
														,snack 	= snack
													)
		
		serializer = SnackPopularitySerializer(popularity)

		return Response(serializer.data)

@api_view(['PUT','POST'])
def purchase(request, snack_id, user_id, format = None):
	try:
		snack = Snack.objects.get(pk=snack_id)
	except Snack.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	try: 
		user = User.objects.get(pk= user_id)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT' or request.method == 'POST':
		if 'quantity' in request.data.keys():
			new_stock_quantity = snack.stock_quantity - int(request.data['quantity'])
			snack.stock_quantity = new_stock_quantity
			serializer = SnackSerializer(snack, data = {'stock_quantity': new_stock_quantity})
			
			if serializer.is_valid():
				serializer.save()

				Purchase.objects.create(
											user 		= user 
											,snack 		= snack
											,quantity 	= new_stock_quantity
										)
				return Response(serializer.data)
		
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
				return Response(status=status.HTTP_400_BAD_REQUEST)	

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk,format = None):
	try:
		user = User.objects.get(pk=pk)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = UserSerializer(user)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def purchase_list(request,format = None):
	if request.method == 'GET':
		purchase = Purchase.objects.all()
		serializer = PurchaseSerializer(purchase, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = PurchaseSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


