# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
def home(request):
	return render(request, "home.html", {})

def about(request):
	return render(request, "about.html", {})

def contact(request):
	return render(request, "contact.html", {})
# Create your views here.
