from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Item

from django.db.models import Q

# Create your views here.


def all_items(request):
    """ Shows all items, including sorting and search queries """

    items = Item.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You must enter a search word")
                return redirect(reverse('items'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            items = items.filter(queries)

    context = {
        'items': items,
        'search_term': query,
    }

    return render(request, 'items/items.html', context)

    context = {
        'items': items,
    }

    return render(request, 'items/items.html', context)


def item_detail(request, item_id):
    """ Shows individual item details """

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'items/item_detail.html', context)
