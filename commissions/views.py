from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Commissions


def all_commissions(request):
    """ Shows all commissions, including search queries """

    commissions = Commissions.objects.all()
    query = None

    if 'q' in request.GET:

        query = request.GET['q']
        if not query:
            messages.error(request, "You must enter a search word")
            return redirect(reverse('commissions'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        commissions = commissions.filter(queries)

    context = {
        'commissions': commissions,
        'search_term': query,
    }

    return render(request, 'commissions/commissions.html', context)