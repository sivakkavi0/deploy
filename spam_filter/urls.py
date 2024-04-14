# spam_detector_app/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('Spam', views.prediction, name='prediction'),
    path('predict', views.predict, name='predict'),
    path('about', views.about, name='about'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
