from django.shortcuts import render
from shop.models import Products
from django.core.paginator import Paginator


# Create your views here.
def index(request):
  productObjects = Products.objects.all()

  # Search
  itemName = request.GET.get('itemName')
  if itemName != '' and itemName is not None:
    productObjects = productObjects.filter(title__icontains = itemName)

  # Pagination
  paginator = Paginator(productObjects, 4)
  page = request.GET.get('page')
  productObjects = paginator.get_page(page)
  return render(request, 'shop/index.html', {'productObjects': productObjects})