from django.urls import path

from . import views

app_name = 'voiceRecorder'
urlpatterns = [
    path('', views.index, name='index'),
    path('train/', views.train, name='train'),
    path('result/', views.result, name='result'),
    path('thanks/', views.thanks, name='result'),
]