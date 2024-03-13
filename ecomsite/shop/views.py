from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_objects = Products.objects.all()

    #SearchFilter
    item_name =  request.GET.get('item_name')
    if item_name != '' and item_name is not None :
        product_objects = product_objects.filter(title__icontains=item_name)
    
    
    #PaginatorCode
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    
    return render(request,'shop/index.html',{'product_objects':product_objects})


def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        number = request.POST.get('number',"")
        address = request.POST.get('address',"")
        landmark = request.POST.get('landmark',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        postalcode = request.POST.get('postalcode',"")
        total = request.POST.get('total',"")

        order =  Order(items=items, name=name, email=email, number=number, address=address,landmark=landmark, city=city, state=state, postalcode=postalcode, total=total)
        order.save()

        return render(request,'shop/checkout.html')
        

    return render(request,'shop/checkout.html')
