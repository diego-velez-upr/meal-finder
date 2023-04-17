from django.shortcuts import render, redirect


def index(request):
    # Check if the user is already logged in, redirect to authentication page if not.
    if not request.user.is_authenticated:
        print('User is not logged in')
        return redirect('/auth/')
    return render(request, 'template.html')
