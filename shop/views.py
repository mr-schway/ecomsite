from django.shortcuts import render
from shop.models import Order, Products
from django.core.paginator import Paginator


# Create your views here.
def index(request):
  productObjects = Products.objects.all()

  # Search
  itemName = request.GET.get('itemName')
  if itemName is None and 'itemName' in request.session:
    itemName = request.session['itemName']
  request.session['itemName'] = itemName
  if itemName != '' and itemName is not None:
    productObjects = productObjects.filter(title__icontains = itemName)

  # Pagination
  paginator = Paginator(productObjects, 4)
  page = request.GET.get('page')
  productObjects = paginator.get_page(page)
  return render(request, 'shop/index.html', {'productObjects': productObjects})


def detail(request, id):
  productObject = Products.objects.get(id=id)
  return render(request, 'shop/detail.html', {'productObject': productObject})

def checkout(request):

  if request.method == "POST":
    items = request.POST.get("items", "")
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    address = request.POST.get("address", "")
    city = request.POST.get("city", "")
    state = request.POST.get("state", "")
    zipcode = request.POST.get("zipcode", "")
    total = request.POST.get("total", "")

    order = Order(
      items = items,
      name = name,
      email = email,
      address = address,
      city = city,
      state = state,
      zipcode = zipcode,
      total = total
    )
    order.save()

  return render(request, 'shop/checkout.html')