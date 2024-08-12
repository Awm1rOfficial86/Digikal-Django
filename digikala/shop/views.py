from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    Slider_Item = SliderItem.objects.all()
    Product_Items = Product.objects.all()
    Category_Items = Category.objects.all()
    Advertising1_Item = Advertising1.objects.all()
    Advertising2_Item = Advertising2.objects.all()
    for Item in Product_Items:
        Pr_It = Item.Price
        PrOf_It = Item.OfferPrice
        a = PrOf_It / Pr_It
        p = a * 100
        k = 100 - p
        limit_t = k <= 43



    return render(request, 'main/index.html', {'Slider_Item': Slider_Item, 'Product_Item': Product_Items,
    'Tkhfif': k, 'limit_t': limit_t, 'Category_Items': Category_Items, 'Advertising1_Item': Advertising1_Item, 'Advertising2_Item': Advertising2_Item})
