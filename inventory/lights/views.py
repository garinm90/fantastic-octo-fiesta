from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import LightLog

# Create your views here.
def index(request):
    return HttpResponse("Light inventory")


class LightLogList(ListView):
    queryset = LightLog.objects.order_by("-date_modified")
