from django.shortcuts import render, redirect
from .models import ContactList_form, Health_form

# Create your views here.
def index(request):
    """This is suppose to show index page"""
    return render(request, 'index.html')

def contact(request):
    """This is suppose to show index page"""
    form = ContactList_form
    return render(request, 'contactList.html', {'form':form})

def health(request):
    """This is suppose to show index page"""
    form = Health_form
    return render(request, 'healthList.html', {'form':form})
