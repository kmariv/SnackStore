# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here
from rest_framework import authentication
from rest_framework import exceptions

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import *
from .serializers import *
from datetime import datetime, timedelta

import json
import ast

def verifyUserLog(req):
	userLog = req['userLog'] if 'userLog' in req.keys() else None
	if userLog is not None:
		userLog = ast.literal_eval(userLog)
	return userLog

def verifyActive(userLog):
	if userLog is not None and datetime.strptime(userLog['session_date'], '%Y-%m-%d %H:%M:%S.%f') >= datetime.now(): 
		return userLog 
	else:
		return None

@api_view(['POST'])
def all_snacks(request,format=None):
	if request.method == 'POST':
		snack = Snack.objects.all()
		serializer = SnackSerializer(snack, many=True)
		return Response(serializer.data)

@api_view(['GET', 'POST'])
def snack_list(request,format = None):
	userLog = verifyUserLog(request.session)

	if request.method == 'GET':
		snack = Snack.objects.all()
		serializer = SnackSerializer(snack, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		if verifyActive(userLog) is not None:
			try:
				user = User.objects.get(pk=userLog['user_id'])
			except User.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)

			if user.is_admin is True:
				serializer = SnackSerializer(data=request.data)
				if serializer.is_valid():
					serializer.save()
					return Response(serializer.data, status=status.HTTP_201_CREATED)
				else:
					return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			else:
				return Response(status=status.HTTP_401_UNAUTHORIZED)
		else:
			return Response(status=status.HTTP_401_UNAUTHORIZED)





@api_view(['GET', 'PUT', 'DELETE'])
def snack_detail(request, pk,format = None):
	userLog = verifyUserLog(request.session)

	try:
		snack = Snack.objects.get(pk=pk)
	except Snack.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = SnackSerializer(snack)
		return Response(serializer.data)

	elif request.method == 'PUT':	
		if verifyActive(userLog) is not None:
			try: 
				user = User.objects.get(username= userLog['username'])
			except User.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)

			if user.is_admin is True:
				serializer = SnackSerializer(snack, data=request.data)
				if serializer.is_valid():
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
			else:
				return Response(status=status.HTTP_401_UNAUTHORIZED)
		else:
			return Response(status=status.HTTP_401_UNAUTHORIZED)
	elif request.method == 'DELETE':
		if verifyActive(userLog) is not None:
			try: 
				user = User.objects.get(username= userLog['username'])
			except User.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)

			if user.is_admin is True:
				snack.delete()
				return Response(status=status.HTTP_204_NO_CONTENT)
			else:
				return Response(status=status.HTTP_401_UNAUTHORIZED)
		else:
			return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def like_product(request, snack_id, format=None):
	userLog = verifyUserLog(request.session)

	if verifyActive(userLog) is not None:
		try:
			snack = Snack.objects.get(pk=snack_id)
		except Snack.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		try: 
			user = User.objects.get(username = userLog['username'])
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
	else:
		return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT','POST'])
def purchase(request, snack_id, format = None):
	userLog = verifyUserLog(request.session)
	if verifyActive(userLog) is not None:
		try:
			snack = Snack.objects.get(pk=snack_id)
		except Snack.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		try: 
			user = User.objects.get(username= userLog['username'])
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
	else:
		return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'POST'])
def user_list(request,format = None):
	if request.method == 'GET':
		user = User.objects.all()
		serializer = UserSerializer(user, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['POST'])
def login(request,format=None):
	try:
		user = User.objects.get(username= request.data['username'])
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	is_auth =  authenticate(request, username=request.data['username'], password=request.data['password'])
	#print request.user
	#request.user = authenticate(request, username='aaaa', password='X')
	#print request.user

	if check_password(str(request.data['password']), user.password) is False or is_auth is None:
		res = {"code": 400, "message": "Password doesn't match with username or User doesn't exist"}
		return Response(data=json.dumps(res), status=status.HTTP_200_OK)
	else:
		serializer = UserSerializer(user)
		dict_token = {
						'user_id': user.user_id
						,'username': user.username
						,'session_date': unicode(datetime.now() + timedelta(minutes = 1))
					}
		dict_token = json.dumps(dict_token)
		request.session['userLog'] = dict_token
		return Response(serializer.data)
