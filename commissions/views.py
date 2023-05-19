from django.shortcuts import render, get_object_or_404
from .models import Commissions


def all_commissions(request):
    """ Shows all commissions """

    commissions = Commissions.objects.all()

    context = {
        'commissions': commissions,
    }

    return render(request, 'commissions/commissions.html', context)


def commission_detail(request, commission_id):
    """ Shows individual commission details """

    commission = get_object_or_404(Commissions, pk=commission_id)

    context = {
        'commission': commission,
    }

    return render(request, 'commissions/commission_detail.html', context)
