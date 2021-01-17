from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_ap.models import UseName
from django_ap.models import AccessData
import json
from datetime import datetime


# Create your views here.
def index(request):
    try:
        var = request.GET.getlist('UserName')[0]
        pas = request.GET.getlist('pass')[0]
        result = UseName.objects.get(user_Name=var, pas=pas)
        return HttpResponse(result)
    except UseName.DoesNotExist:
        return HttpResponse(69)

@csrf_exempt
def createUser(request):
    name = request.GET.get('UserName')
    password = request.GET.get('pass')
    u = UseName(user_Name=name, pas=password)
    u.save()
    return HttpResponse(99)


@csrf_exempt
def get_items(request):
    name = request.GET.get('UserName')
    a = AccessData.objects.get(user=name)
    return HttpResponse(a)


@csrf_exempt
def add_items(request):
    name = request.GET.get('UserName')
    habbit = request.GET.get('habbit')
    d = datetime.now()
    a = AccessData(user=name, item=habbit, date=d, endDate=d)
    a.save()
    print(d)
    return HttpResponse(25)
    






