from django.urls import path, include
from ..views import quiz_views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.results, name='result'),
]
