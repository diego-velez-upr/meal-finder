from django.shortcuts import render
from .models import Food


def index(request):
    """
    The view of the '/' url.
    """

    foods = Food.objects.all()
    # Divides the list of foods into a list of a list of foods, where each inner list has 3 food items.
    # This is done in order to be able to use the html templates easily.
    total = [foods[food_stop - 3:food_stop:] for food_stop in range(3, len(foods), 3)]

    context = {
        "foods": total
    }

    return render(request, 'index.html', context)


def offers(request):
    return render(request, 'offers.html')


def about(request):
    return render(request, 'about.html')


def feedback(request):
    return render(request, 'feedback.html')


def map_request(request):
    return render(request, 'map.html')


def menu(request):
    return render(request, 'menu.html')


def more(request):
    return render(request, 'more.html')


def search(request):
    return render(request, 'search.html')
