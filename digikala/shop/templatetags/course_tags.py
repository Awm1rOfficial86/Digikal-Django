from django import template
import  math
register = template.Library()

@register.simple_tag
def discount_calculation(price,discount):
    sellprice = int(100 - (discount / price * 100))
    return math.floor(sellprice)


@register.simple_tag
def rating(pok):
    if 2 >= pok >= 0:
        return "بد"
    elif 4 >= pok > 2:
        return "خوب"
    elif 5 >= pok > 4:
        return "عالی"

