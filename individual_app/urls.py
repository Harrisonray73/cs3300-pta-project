from django.urls import path
from . import views

urlpattern =[
    # difines the url pattern '' is empty represents
    # the path to app views, index is the function 
    # defined in view.py name='index' is dynamic.
    path('', views.index, name='index'),
]