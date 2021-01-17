from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_ap.models import UseName
from django_ap.models import AccessData
from django_ap.models import DoneData
import json
from datetime import datetime
from django.core import serializers



# Create your views here.
def index(request):
    try:
        var = request.GET.get('UserName')
        pas = request.GET.get('pass')
        result = UseName.objects.get(user_Name=var, pas=pas)
        dic = {}
        dic['userName'] = result.user_Name
        dic['password'] = result.pas
        return JsonResponse(dic)
    except UseName.DoesNotExist:
        return HttpResponse(69)

@csrf_exempt
def createUser(request):
    name = request.GET.get('UserName')
    password = request.GET.get('pass')
    u = UseName(user_Name=name, pas=password)
    u.save()
    return HttpResponse(95)


@csrf_exempt
def get_items(request):
    try:
        name = request.GET.get('UserName')
        a = AccessData.objects.filter(user=name)
        data = {}
        for values in a:
            data['name'] = values.user;
            data['habbit'] = values.item;
            data['date'] = values.date;
            data['endDate'] = values.endDate;
  
        return JsonResponse(data)
    except AccessData.DoesNotExist:
        return HttpResponse(29)
        


@csrf_exempt
def add_items(request):
    name = request.GET.get('UserName')
    habbit = request.GET.get('habbit')
    d = datetime.now()
    a = AccessData(user=name, item=habbit, date=d, endDate=d)
    a.save()
    print(d)
    return HttpResponse(25)

@csrf_exempt
def doneItems(request):
    name = request.GET.get('name')
    doneHabbit = request.GET.get('habbit')
    dataHabbit = AccessData.objects.get(user=name, item=doneHabbit)
    dataHabbit.delete()
    id = 2
    id = id + 1
    d = datetime.now()
    result = DoneData(id, name, doneHabbit, d)
    result.save()
    print(result)
    return HttpResponse(2)

@csrf_exempt
def getDoneItems(request):
     try:
        name = request.GET.get('name')
        a = DoneData.objects.filter(user=name)
        data = {}
        for values in a:
            data['name'] = values.user
            data['item'] = values.item
            data['date'] = str(values.dateEnded)
        dumps = json.dumps(data)
        return JsonResponse(dumps, safe=False)
     except DoneData.DoesNotExist:
        return HttpResponse(39)
        








