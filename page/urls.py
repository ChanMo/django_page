from django.urls import path
from .views import *

urlpatterns = [
    path('api/<slug:slug>/', PageView.as_view()),
    path('<slug:slug>/', page_view)
]
