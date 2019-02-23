# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

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
		serializer = SnackSerializer(snack, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		snack.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

