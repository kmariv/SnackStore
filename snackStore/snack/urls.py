from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snack import views

urlpatterns = [
    url(r'^getSnack/$', views.snack_list,name="snack-list"),
    url(r'^getSnack/(?P<pk>[0-9]+)/', views.snack_detail,name="snack-detail"),
    url(r'^user/(?P<pk>[0-9]+)/', views.user_detail,name="user-detail"),
    url(r'^purchase/$', views.purchase_list, name="purchase-list"),
    url(r'^purchase/(?P<snack_id>[0-9]+)/(?P<user_id>[0-9]+)/', views.purchase, name="purchase"),
    url(r'^like/(?P<snack_id>[0-9]+)/(?P<user_id>[0-9]+)/', views.like_product, name="like-product"),
]

urlpatterns = format_suffix_patterns(urlpatterns)