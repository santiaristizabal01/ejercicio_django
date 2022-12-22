from django.http import HttpResponse
from django.shortcuts import render

import random

def recuperatorio(request):
    array = [1,2,4,67,2,4,-7,-2,12,0,30,22,98]
    random.shuffle(array)
    return render(request,"ejercicio.html", {"array": array})
    # return HttpResponse("Recuperatorio")