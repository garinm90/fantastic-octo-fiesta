from django.urls import path
from .views import LightLogList

urlpatterns = [path("", LightLogList.as_view())]

