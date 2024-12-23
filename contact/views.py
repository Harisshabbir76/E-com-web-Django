from django.shortcuts import render,redirect
from .models import Contact
from . import forms

def contact(request):
    if request.method=='POST':
        form=forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Contact:contact')
    else:
        form=forms.ContactForm()
    return render (request, 'contact/contact.html',{'form':form})