from django.urls import path
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('members/', views.MemberListView.as_view(), name= 'members'),
path('member/<int:pk>/', views.MemberDetailView.as_view(), name='member-detail'),
path('position/<int:pk>/', views.PositionDetailView.as_view(), name='position-detail'),
]