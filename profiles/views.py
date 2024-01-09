from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, FavouriteBowls
from checkout.models import Order
from products.models import Product

from .forms import UserProfileForm

@login_required
def profile(request):
    """ Display the user's profile. """
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Get or create the user's favourite bowls
    favourite_bowls, created = FavouriteBowls.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=user_profile)

    orders = user_profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'favourite_bowls': favourite_bowls.bowls.all(),
        'on_profile_page': True,
    }

    return render(request, template, context)



def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def add_to_favourites(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    favourite_bowls, created = FavouriteBowls.objects.get_or_create(user=request.user)

    if product in favourite_bowls.bowls.all():
        messages.warning(request, f"{product.name} is already in your favorites.")
    else:
        favourite_bowls.bowls.add(product)
        messages.success(request, f"{product.name} added to your favorites.")

    return redirect('profile')


@login_required
def remove_from_favourites(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    favourite_bowls = FavouriteBowls.objects.get(user=request.user)

    if product in favourite_bowls.bowls.all():
        favourite_bowls.bowls.remove(product)
        messages.success(request, f"{product.name} removed from your favorites.")
    else:
        messages.warning(request, f"{product.name} is not in your favorites.")

    return redirect('profile')


