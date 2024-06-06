from django.shortcuts import render

# Create your views here.

def order_view(request):
    return render(request, 'orders/shopping.html')