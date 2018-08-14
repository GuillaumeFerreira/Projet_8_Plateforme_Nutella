from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
	
	
	return render(request,'./index.html')
	
def resultat(request):
	return render(request,'./resultat.html')
	
def aliment(request):
	return render(request,'./aliment.html')
	
def compte(request):
	return render(request,'./compte.html')