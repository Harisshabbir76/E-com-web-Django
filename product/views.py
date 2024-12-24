from django.shortcuts import render,redirect
from .models import Products,Order
from .forms import OrderForm
from django.shortcuts import get_object_or_404




def Home(request):
    products=Products.objects.all()
    return render (request, 'product/product.html', {'prodcuts':products})




def ProductDetail(request, slug):
    product = get_object_or_404(Products, slug=slug)
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
    return render (request, 'product/cart.html')