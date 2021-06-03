from django.urls import path
from .views import home_view, detail_view, tagged, homepage, test, blog_sport, blog_weight_lost, like
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('blog/', home_view, name="home"),
    path('blog/post/<slug:slug>/', detail_view, name="detail"),
    path('like/<slug:slug>/', like, name='postlike'),
    path('blog/tag/<slug:slug>/', tagged, name="tagged"),
    path('', homepage, name='blog_homepage'),
    path('sport', blog_sport),
    path('weight_lost', blog_weight_lost),
    path('test/', test),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
