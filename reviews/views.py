from django.shortcuts import render, get_object_or_404
from items.models import Item
from .models import Review
from profiles.models import UserProfile


def reviews(request, item_id):
    """ A view to show all available reviews for current item """
    item = get_object_or_404(Item, pk=item_id)

    reviews = Review.objects.filter(item=item)
    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
        'item': item,
    }

    return render(request, template, context)
