from django.shortcuts import render,redirect
from .models import Products,Order,CartItem
from .forms import OrderForm
from django.shortcuts import get_object_or_404




def Home(request):
    products=Products.objects.all()
    return render (request, 'product/product.html', {'prodcuts':products})


def ProductDetail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    session_key = request.session.session_key

    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    if request.method == 'POST':
        if 'add_to_cart' in request.POST:  # Check which button was clicked
            quantity = int(request.POST.get('quantity', 1))
            cart_item, created = CartItem.objects.get_or_create(
                session_key=session_key,
                product=product
            )
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            return redirect('Products:cart')  # Redirect to cart page

        elif 'order_now' in request.POST:  # "Order Now" button clicked
            return redirect('Products:Order', slug=slug)  # Redirect to Order form page

    return render(request, 'product/product_detail.html', {'product': product})



def Order(request, slug):
    product = get_object_or_404(Products, slug=slug)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = int(request.POST.get('quantity',1))  
            order = form.save(commit=False)
            order.product = product
            order.quantity = quantity 
            order.total_price = product.price * quantity  
            order.save() 

            return render(request, 'product/order_confirmation.html', {
                'order': order,
                'quantity': quantity,
                'total_price': order.total_price
            })
    else:
        form = OrderForm()

    return render(request, 'product/order.html', {
        'product': product,
        'form': form
    })





def checkOut(request, slug):
    product = get_object_or_404(Products, slug=slug)
    order = Order.objects.filter(product=product)
    if order:
        return render(request, 'product/order_confirmation.html', {
            'order': order,
            'quantity': order.quantity,
            'total_price': order.total_price,
        })
    else:
        return redirect('Products:home')    


def Cart(request):
    session_key = request.session.session_key
    if not session_key:
        cart_items = []
    else:
        cart_items = CartItem.objects.filter(session_key=session_key)

    if request.method == 'POST':
        # Clear the cart or process the order
        if cart_items.exists():
            first_item_slug = cart_items.first().product.slug
            cart_items.delete()
            return redirect('Products:Order', slug=first_item_slug)
        else:
            return redirect('Products:home')  # Redirect to home if no items in the cart

    return render(request, 'product/cart.html', {'cart_items': cart_items})
