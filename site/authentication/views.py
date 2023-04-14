from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from meal_finder import settings


# Create your views here.
def home(request):
    return render(request, "index.html")


def signup(request):
    # If the user enters all the info and clicks sign up, all the info is saved and then a new user is created
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered")
            return redirect('home')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")

        if pass1 != pass2:
            messages.error(request, "Password do not match")

        if not username.isalnum():
            messages.error(request, "Username must be Alphanumeric")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)  # creating new user
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()  # saving new user

        messages.success(request,
                         "Your account has been succesfully created! We have sent you a confirmation email, please confirm your email in order to activate your account")

        # Welcome Email

        subject = "Welcome to College Bites!"
        message = "Hello " + myuser.first_name + "!! \n" + "Thank you for using College Bites \n We sent you a confirmation email, please confirm your email address in order to activate your account"
        # BUG: Infinitely loads then crashes because host email doesn't exist
        # REPLY: Added again for testing
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        # Potential bugs: from_email and to_list line above
        return redirect('signin')

    return render(request, "signup.html")  # Enters the signup page


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,
                            password=pass1)  # If the user is not authenticated, it will return a None variable

        if user is not None:  # If the user is authenticated, do the login
            login(request, user)
            fname = user.first_name
            return render(request, "template.html")

        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')

    return render(request, "signin.html")  # Enters the sign in page


def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('home')
