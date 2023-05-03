from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from items.models import Item, Category
from .models import Commissions


def all_commissions(request):
    """ Shows all commissions, including search queries """

    commissions = Commissions.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            commissions = commissions.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You must enter a search word")
                return redirect(reverse('commissions'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            commissions = commissions.filter(queries)

    context = {
        'commissions': commissions,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'commissions/commissions.html', context)


def commission_detail(request, commission_id):
    """ Shows individual commission details """

    commission = get_object_or_404(Commissions, pk=commission_id)

    context = {
        'commission': commission,
    }

    return render(request, 'commissions/commission_detail.html', context)
