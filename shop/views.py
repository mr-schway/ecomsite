from django.shortcuts import render
from shop.models import Products


# Create your views here.
def index(request):
  productObjects = Products.objects.all()
  return render(request, 'shop/index.html', {'productObjects': productObjects})