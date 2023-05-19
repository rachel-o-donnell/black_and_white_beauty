from django.shortcuts import render, get_object_or_404, redirect, reverse
from items.models import Item
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
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


def add_review(request, item_id):
    """
    Allow users to add a review
    """
    if not request.user.is_authenticated:
        messages.error(request,
                       'You need to be logged in to add a review.')
        return redirect(reverse('account_login'))

    user = UserProfile.objects.get(user=request.user)
    item = Item.objects.get(id=item_id)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)

        if form.is_valid():
            review = form.save()
            review.item = item
            review.user = request.user
            review.save()
            messages.success(
                request, f"Your review for '{item.name}' has been submitted!")
            return redirect(reverse('item_detail', args=[item.id]))
        else:
            messages.error(
                request, "Yikes, something went wrong."
                " Please ensure your fields are valid")
            return redirect(reverse('item_detail', args=[item.id]))
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'

    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    Admin can delete reviews
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)

    review.delete()

    messages.success(
        request, f'You deleted the review titled: "{ review.title }"')
    return redirect(reverse('items'))
