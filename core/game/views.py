from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request) -> HttpResponse:
    return render(request, 'base.html')
