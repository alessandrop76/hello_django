from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<div style="background-color:red"'
                        '<h1>Hello {} de {} anos</h></div>'.format(nome, idade))