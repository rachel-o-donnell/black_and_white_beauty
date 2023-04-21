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
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    messages.success(request, f'You added {quantity} x "{item.name}" to your cart.')
    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified item to the specified amount"""

    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Cart updated. You now have {quantity} x "{item.name}" in your cart.')
    else:
        cart.pop(item_id)
        messages.success(request, f'You added {quantity} x "{item.name}" to your cart')

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
        messages.error(request, f'An error occured removing "{e}" from your cart')
        return HttpResponse(status=500)
