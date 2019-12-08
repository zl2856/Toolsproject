from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('', views.list),
    path('add', views.add),
    path('stats', views.stats),
    path('<unique_squirrel_id>', views.update),
]



