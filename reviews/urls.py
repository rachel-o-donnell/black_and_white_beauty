from django.urls import path
from . import views

urlpatterns = [
    path('reviews/<int:item_id>', views.reviews, name='reviews'),

]
