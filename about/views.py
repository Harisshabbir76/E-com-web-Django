from django.shortcuts import render


def About(request):
    return render (request, 'about/about.html')