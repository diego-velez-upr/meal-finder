from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def listing(request):
    return render(request, 'listing.html')


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
