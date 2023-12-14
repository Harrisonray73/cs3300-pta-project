from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Member, Position
# Create your views here.
def index(request):

    # Your view logic here
   member_active_accounts = Member.objects.select_related('member').all().filter(member__is_active=True)
   print("active individual query set", member_active_accounts)
   return render(request, 'individual_app/index.html', {'member_active_accounts':member_active_accounts})
# Render index.html

#return render( request, 'individual_app/base_template.html')

class MemberListView(generic.ListView):
   model = Member

class MemberDetailView(generic.DetailView):
   model = Member

class PositionDetailView(generic.DetailView):
   model = Position
   def get_context_data(self, **kwargs):
       # Call the base implementation first to get the context
       context = super(PositionDetailView, self).get_context_data(**kwargs)
   