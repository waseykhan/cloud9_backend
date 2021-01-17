from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_ap.models import UseName
import json





# Create your views here.
def index(request):
    try:
        var = request.GET.getlist('UserName')[0]
        pas = request.GET.getlist('pass')[0]
        #uName = UseName(user_Name="var", pas="pas")
        result = UseName.objects.get(user_Name=var, pas=pas)
        #print(uName.objects.all())
        return HttpResponse(result)
    except UseName.DoesNotExist:
        return HttpResponse(69)


    
    






