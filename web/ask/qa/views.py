from django.shortcuts import render


from django.http import HttpResponse 

# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('\nOK\n\n')

def aaa(request, *args, **kwargs):
    return HttpResponse('\nHello, from aaa!\n\n')



def aaa222(request, *args, **kwargs):
    return HttpResponse('\nHello, from a2222!\n\n')


#####
# from example https://djbook.ru/rel1.9/intro/tutorial01.html
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
#####