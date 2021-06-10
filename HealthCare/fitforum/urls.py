from django.contrib import admin
from django.urls import path,include
import fitforum.views as fitforum
from fitforum.views import fitness,yoga

urlpatterns = [
    path('',fitforum.index,name='fitforum'),
    path('fitness/',fitforum.fitness,name='fitness'),
    path('<int:tvno>/',fitforum.fitness,name='tv-url'),
    path('<int:tvno>/',fitforum.fitness,name='tvno-url'),
    path('yoga/',fitforum.yoga,name='yoga'),
    path('yoga/<int:tvno>/',fitforum.yoga,name='yoga-url'),
]
