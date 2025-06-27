from django.shortcuts import render
from shop.models import Products


# Create your views here.
def index(request):
  productObjects = Products.objects.all()

  itemName = request.GET.get('itemName')
  if itemName != '' and itemName is not None:
    productObjects = productObjects.filter(title__icontains = itemName)
  return render(request, 'shop/index.html', {'productObjects': productObjects})