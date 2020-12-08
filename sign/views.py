from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('hello django!')


def index_html(request):
    return render(request,'index.html')