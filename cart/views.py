from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from items.models import Item


def view_cart(request):
    """ A view to return the shopping-cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified item to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    item = get_object_or_404(Item, pk=item_id)

    if item_id in list(cart.keys()):
        if cart[item_id] + quantity > 99:
            cart[item_id] = 99
        else:
            cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    """ Prevent anyone ordering more than the limit of 99 items or entering /
        negative values"""
    if quantity > 99:
        messages.error(
            request,
            f"You cannot have more than 99 { item.name }'s in your cart."
        )

    elif quantity < 0:
        messages.error(
            request,
            "You cannot add negative quantities. Please remove the item"
            " using the 'Remove' button or update the number of items."
        )

    elif quantity > 0:
        if cart[item_id] + quantity > 99:
            messages.error(
                request,
                f"You cannot have more than 99 { item.name }'s in your cart."
            )
        elif cart[item_id] + quantity < 0:
            messages.error(
                request,
                'You cannot add negative quantities. Please remove the item'
                ' using the "Remove" button or update the number of items.'
            )
        else:
            cart[item_id] = quantity
            messages.success(
                request, f'You added {quantity} x "{item.name}" to your cart.')  # noqa
    else:
        messages.success(
            request, f'You added {quantity} x "{item.name}" to your cart.')  # noqa
    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified item to the specified amount"""

    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    """ Prevent anyone ordering more than the limit of 99 items or entering /
        negative values"""
    if quantity > 99:
        messages.error(
            request,
            f"You cannot have more than 99 { item.name }'s in your cart."
        )

    elif quantity < 0:
        messages.error(
            request,
            "You cannot add negative quantities. Please remove the item"
            " using the 'Remove' button or update the number of items."
        )

    elif quantity > 0:
        if cart[item_id] + quantity > 99:
            messages.error(
                request,
                f"You cannot have more than 99 { item.name }'s in your cart."
            )
        elif cart[item_id] + quantity < 0:
            messages.error(
                request,
                'You cannot add negative quantities. Please remove the item'
                ' using the "Remove" button or update the number of items.'
            )
        else:
            cart[item_id] = quantity
            messages.success(
                request, f'You now have {quantity} x "{item.name}" in your cart')  # noqa
    else:
        cart.pop(item_id)
        messages.success(
            request, f'You now have {quantity} x "{item.name}" in your cart')
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    item = get_object_or_404(Item, pk=item_id)
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'"{item.name}" removed from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request, f'An error occured removing "{e}" from your cart')
        return HttpResponse(status=500)
