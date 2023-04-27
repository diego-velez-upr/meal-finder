from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Food
from .utils.food_utils import search_food
from .utils.list_utils import divide_into_sublist


@csrf_exempt
def apply_filters(request):
    """
    Used when updating the food filters, returns the HTML of the table that contains the food with the filter applied.
    """

    foods = Food.objects.all()
    filters = request.GET.get('filters')

    # Check if there are filters applied
    if filters is not None:
        foods = search_food(foods, filters, delimiter=',')

    divided_foods = divide_into_sublist(foods, 3)

    context = {
        "foods": divided_foods
    }

    return render(request, 'table_list.html', context)


def listing(request):
    """
    The view of the '/' url.
    """

    # Check if the user is already logged in, redirect to authentication page if not.
    if not request.user.is_authenticated:
        print('User is not logged in')
        return redirect('/auth/')

    foods = Food.objects.all()
    # Divides the list of foods into a list of a list of foods, where each inner list has 3 food items.
    # This is done in order to be able to use the html templates easily.
    divided_foods = divide_into_sublist(foods, 3)

    context = {
        "foods": divided_foods
    }

    return render(request, 'listing.html', context)


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
