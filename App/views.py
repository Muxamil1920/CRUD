from django.shortcuts import render
from . models import Products

# Create your views here.

def index(request):
    products = Products.objects.all()
    return render(request, 'index.html', {'products':products})

def product_list(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        file = request.POST.get('file')
        
        
        product_list = Products(name=name,price=price,description=description,file=file)
        product_list.save()
        
    return render(request,'sucess.html')
                
       
