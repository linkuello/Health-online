"""HealthCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import home_view, detail_view, tagged, homepage, test, blog_sport, blog_weight_lost
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', home_view, name="home"),
    path('blog/post/<slug:slug>/', detail_view, name="detail"),
    path('blog/tag/<slug:slug>/', tagged, name="tagged"),
    path('', homepage),
    path('sport', blog_sport),
    path('weight_lost', blog_weight_lost),
    path('test/', test),

] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
