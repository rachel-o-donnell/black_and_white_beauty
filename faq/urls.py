from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq_view, name='faq_view'),
]
