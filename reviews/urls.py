from django.urls import path
from . import views

urlpatterns = [
    path('reviews/<int:item_id>', views.reviews, name='reviews'),
    path('add_review/<int:item_id>', views.add_review, name='add_review'),
]
