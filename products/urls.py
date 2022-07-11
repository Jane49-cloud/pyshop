from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('goods', views.goods),
    path('contact', views.contact),
]

