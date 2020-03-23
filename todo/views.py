#import the django package that handles views/requests
from django.shortcuts import render
from .models import List

#VIEWS

#function that renders and returns the 'home' page
def home(request):
	all_items = List.objects.all
	return render(request, 'home.html', {'all_items': all_items})

#function that renders and returns the 'about' page
def about(request):
	my_name = "Seadna"
	return render(request, 'about.html', {'name': my_name})



