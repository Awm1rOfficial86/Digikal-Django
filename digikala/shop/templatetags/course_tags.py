from django import template
import  math
register = template.Library()

@register.simple_tag
def discount_calculation(price,discount):
    sellprice = int(100 - (discount / price * 100))
    return sellprice

