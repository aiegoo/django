from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def post_home(request):
     return HttpRequest("<h1>hello</h1>")