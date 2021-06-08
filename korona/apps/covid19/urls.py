from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1/', views.chart, name='chart'),
    path('nyuryoku/', views.nyuryoku, name='nyuryoku'),
]