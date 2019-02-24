# -*- encoding: utf-8 -*-

from django.shortcuts import render

def SnackStoreViews(request):
	return render(request, 'snack_store.html',{})