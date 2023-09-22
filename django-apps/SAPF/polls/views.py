from django.shortcuts import render

from django.http import HttpResponse

#def paginainicial(request):
    #return render(request, 'paginas/login.html')

# Create your views here.

def index(request):
    return HttpResponse('tryutyu')
