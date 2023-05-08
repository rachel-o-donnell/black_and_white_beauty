from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq_view, name='faqs'),
    path('add_faq/', views.add_faq, name='add_faq'),
    path('edit_faq/<int:faq_id>/', views.edit_faq, name='edit_faq'),
    path('delete_faq/<int:faq_id>/', views.delete_faq, name='delete_faq'),
]
