from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_commissions, name='commissions'),
    path('<int:commission_id>/', views.commission_detail, name='commission_detail'),
]
