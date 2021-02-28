'''
===========================================================
This is an added file to be imported by urls.py in the myblogsite 
===========================================================
'''
from django.urls import path
from . import views

urlpatterns = [
    # 
    path('', views.post_list, name='post_list'),
]
