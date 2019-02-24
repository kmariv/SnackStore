from django.conf.urls import url
from client_views import *

urlpatterns = [
    url(r'^store/$', SnackStoreViews, name="store"),
]