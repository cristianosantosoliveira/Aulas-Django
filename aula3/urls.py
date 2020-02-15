

from django.urls import path
from .views import index, setacookie, HttpResponseRedirect
from aula3.views import redireciona

app_name =  "aula3"

urlpatterns = [
    path('', index),
    path('cookie', setacookie),
    path('uol', redireciona),
]
