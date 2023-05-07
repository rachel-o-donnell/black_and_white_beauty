from django.shortcuts import render
from . models import Faq


def faq_view(request):
    """ FAQ's page view"""

    faq = Faq.objects.all().order_by('-date')
    context = {
        'faq': faq
    }
    template = 'faq/faq.html'

    return render(request, template, context)
