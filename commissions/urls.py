from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_commissions, name='all_commissions'),
]
