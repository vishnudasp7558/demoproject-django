from shop.models import Shop


def links(request):
    c=Shop.objects.all()
    return {'links':c}