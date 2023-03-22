from django.shortcuts import render
from .models import Food


def index(request):
    """
    The view of the '/' url.
    """
    context = {
        "foods": Food.objects.all()
    }
    return render(request, 'template.html', context)
