from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def koti(request):
    return HttpResponse('koti is  all rounder')

def abhijith(request):
    return HttpResponse('abhijith k biju ')
def addres(request):
    return HttpResponse('kandathinkarayil(h) puthupparayaram p.o thodupuzha kerala')