from django.shortcuts import render


from django.http import HttpResponse 

# Create your views here.

def test(request, *args, **kwargs):
<<<<<<< HEAD
    return HttpResponse('\nOK\n\n')

def aaa(request, *args, **kwargs):
    return HttpResponse('\nHello, from aaa!\n\n')



def aaa222(request, *args, **kwargs):
    return HttpResponse('\nHello, from a2222!\n\n')
=======
    return HttpResponse('OK')

def aaa(request, *args, **kwargs):
    return HttpResponse('AAA')
>>>>>>> 2ab6c2dc0cdfd91ada8694f15d5499163a52a21d


#####
# from example https://djbook.ru/rel1.9/intro/tutorial01.html
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
#####