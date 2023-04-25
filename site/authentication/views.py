from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, render


# Create your views here.
def home(request):
    return render(request, "authentication.html")


def sign_up(request):
    # If the user enters all the info and clicks sign up, all the info is saved and then a new user is created
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists!")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')

        # TODO: doesn't seem to do anything
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters!")
            return redirect('signup') #  Django only permits 30 character usernames but to keep it more clean a 10 character limit is forced

        # BUG: Crashes when passwords are not the same
        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric!")
            return redirect('signup')

        # Create user and save to database
        user = User.objects.create_user(username, email, pass1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Welcome Email
        subject = "Welcome to College Bites!"
        message = "Hello " + user.first_name + "!! \n" + "Thank you for using College Bites \n We sent you a confirmation email, please confirm your email address in order to activate your account"
        # BUG: Infinitely loads then crashes because host email doesn't exist
        # Reply: Also I think it makes it crash, maybe sending an email for verification isnt viable at this stage of the project? I commented the lines that made signing in work.
        #recipient_list = [user.email]
        #send_mail(subject, message, None, recipient_list, fail_silently=False)

        messages.success(request, "Your account has been successfully created!")

        return redirect('signin')

    return render(request, "signup.html")  # Enters the signup page


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # If the user is not authenticated, it will return a None variable
        user = authenticate(username=username, password=password)

        # If the user failed to log in, then redirect back to authentication page, otherwise log the user in
        # and redirect to listing page
        if user is None:
            messages.error(request, "Bad Credentials")
            return redirect('home')

        login(request, user)
        return redirect('/')

    return render(request, "signin.html")


def sign_out(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('home')
