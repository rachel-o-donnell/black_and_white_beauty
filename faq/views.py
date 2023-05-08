from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Faq
from . forms import FaqForm


def faq_view(request):
    """ FAQ's page view"""

    faq = Faq.objects.all().order_by('-date')
    context = {
        'faq': faq
    }
    template = 'faq/faqs.html'

    return render(request, template, context)


@login_required
def add_faq(request):
    """ Displays the form for admin to add a FAQ """

    if not request.user.is_superuser:
        messages.error(request, 'Access is only authorised for store owners')
        return redirect(reverse('home'))

    faqs = Faq.objects.all()

    if request.method == 'POST':
        form = FaqForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added FAQ!')
            return redirect(reverse('add_faq'))
        else:
            messages.error(
                request, 'Something went wrong, Please ensure the form is valid.')
    else:
        form = FaqForm()
    template = 'faq/add_faq.html'
    context = {
        'form': form,
        'faqs': faqs,
    }
    return render(request, template, context)


@login_required
def edit_faq(request, faq_id):
    """ Lets admin edit a faq  """

    if not request.user.is_superuser:
        messages.error(request, 'Access is only authorised for store owners')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated faq!')
            return redirect(reverse('faqs'))
        else:
            messages.error(
                request, 'Something went wrong, Please ensure the form is valid.')
    else:
        form = FaqForm(instance=faq)

    template = 'faq/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """ Delete a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Access is only authorised for store owners')
        return redirect(reverse('faqs'))

    faq = get_object_or_404(Faq, pk=faq_id)
    faq.delete()
    messages.success(request, f'You successfully deleted {faq.question}')

    return redirect(reverse('faqs'))
