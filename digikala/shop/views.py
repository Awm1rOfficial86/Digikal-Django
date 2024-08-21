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
    News_Items = News.objects.all()

    return render(request, 'main/index.html', {'Slider_Item': Slider_Item, 'Product_Item': Product_Items,
                                               'Category_Items': Category_Items,
                                               'Advertising1_Item': Advertising1_Items,
                                               'Advertising2_Item': Advertising2_Items, 'Prit': Product_Items,
                                               'News_Items': News_Items})


def single(request, id):
    Sin_Id = Product.objects.get(id=id)
    Color_Item = Color.objects.all()
    Color_Item2 = Color2.objects.all()
    Color_Item3 = Color3.objects.all()
    Color_Item4 = Color4.objects.all()
    Color_Item5 = Color5.objects.all()
    return render(request, 'main/single.html',
                  {'Sin_Id': Sin_Id, 'Color_Item': Color_Item, 'Color_Item2': Color_Item2, 'Color_Item3': Color_Item3,
                   'Color_Item4': Color_Item4, 'Color_Item5': Color_Item5})


def product(request):
    Product_Items = Product.objects.all()
    return render(request, 'main/product.html', {'Product_Items': Product_Items})

def footer(request):
    Product_Items = Product.objects.all()
    return render(request, 'main/footer.html', {'Product_Items': Product_Items})



