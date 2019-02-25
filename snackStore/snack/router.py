# -*- coding: utf-8 -*-
from .viewsets import * 
from rest_framework import routers 

router = routers.DefaultRouter()

router.register('getSnacks', SnackViewSet, base_name='getSnack')