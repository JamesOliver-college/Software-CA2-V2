from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from cart.forms import CartAddProductForm
import stripe
from vouchers.forms import VoucherApplyForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items = None):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
        'update': True})
    total = int(Cart.get_total_price(cart))
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'Newsstand Purchase'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    voucher_apply_form = VoucherApplyForm()

    return render(request, 'cart/detail.html', {'cart': cart, 'voucher_apply_form': voucher_apply_form}, dict(cart_items = cart_items, total = total, counter = counter, data_key = data_key, stripe_total = stripe_total, description = description))