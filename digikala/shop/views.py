from _ast import Add

from django.shortcuts import render
from .models import *



# Create your views here.
def index(request):
    global k, limit_t
    Slider_Item = SliderItem.objects.all()
    Product_Items = Product.objects.all().order_by('-Count')
    Category_Items = Category.objects.all()
    Advertising1_Items = Advertising1.objects.all()
    Advertising2_Items = Advertising2.objects.all()

    for Item in Product_Items:
        Pr_It = int(Item.Price)
        PrOf_It = int(Item.Price)
        a = PrOf_It / Pr_It
        p = a * 100
        k = 100 - p
        print(k)
        limit_t = k <= 43


    return render(request, 'main/index.html', {'Slider_Item': Slider_Item, 'Product_Item': Product_Items,
    'Tkhfif': k, 'limit_t': limit_t, 'Category_Items': Category_Items, 'Advertising1_Item': Advertising1_Items, 'Advertising2_Item': Advertising2_Items,'Prit':Product_Items})


