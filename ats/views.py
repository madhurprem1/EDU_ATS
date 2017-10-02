# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
# def index(request):
	
# 	return render(request, 'index.html')

# def base(request):
	
# 	return render(request, 'index.html')
def index(request):
	
	return render(request, 'index.html')	
	
def about(request):
	
	return render(request, 'about.html')

def contact(request):
	
	return render(request, 'contact.html')		

# def login(request):
	
# 	return render(request, 'login.html')

