from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snack import views

urlpatterns = [
    url(r'^getSnack/$', views.snack_list),
    url(r'^getSnack/(?P<pk>[0-9]+)/', views.snack_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)