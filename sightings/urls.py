from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin
#from .views import (createpost, detail_post_view, editpost)

urlpatterns = [
        path('', views.list),
        path('<unique_squirrel_id>', views.update),
        path('add', views.create),
        path('stats',views.stats),
        ]



