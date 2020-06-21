from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return render(request, 'homepage/index.html')

def portfolio(request):
	return render(request, 'homepage/portfolio.html')

def contact(request):
	return render(request, 'homepage/contact.html')

