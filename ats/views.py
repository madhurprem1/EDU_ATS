# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from ats.forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template import Context
from django.template.loader import get_template
from django.core.mail import send_mail, BadHeaderError,EmailMessage
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseNotFound
from django import forms
from .forms import ContactForm,SignUpForm
# Create your views here.
# def index(request):
	
# 	return render(request, 'index.html')

# def base(request):
	
# 	return render(request, 'index.html')
def index(request):
	
	return render(request, 'index.html')	

def about(request):
	
	return render(request, 'about.html')
	
def email(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, from_email, ['madhurprem1@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('success')
	return render(request, "email.html", {'form': form})
	
def success(request):
	return HttpResponse('Success! Thank you for your message.')


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('login')
	else:
		form = SignUpForm()
	return render(request, 'sign_up.html', {'form': form})

def password_reset_done(request):
	return render(request, 'password_reset_done.html')

