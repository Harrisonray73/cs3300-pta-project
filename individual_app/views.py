from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Member, Position
# Create your views here.
#def index(request):
def member_view(request):
    # Your view logic here
    return render(request, 'individual_app/base_template.html')
# Render index.html
user_active_accounts = Member.objects.select_related('individual').all().filter(individual__is_active=True)
print("active individual query set", user_active_accounts)
#return render( request, 'individual_app/base_template.html')

class MemberListView(generic.ListView):
    model = Member

class MemberDetailView(generic.DetailView):
    model = Member

class PositionDetailView(generic.DetailView):
    model = Position
