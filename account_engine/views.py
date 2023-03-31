from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.hashers import make_password

from  properties_engine .models import  Property,LatestPg,LatesFlat
from .models import User


def register(request):
    user_type = None
    if request.method == "POST":
        user_type = request.POST.get('user_type')
        username = request.POST.get('username')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if user_type == 'agent':
            user_type = True
        else:
            user_type = False
        encrypted_password = make_password(password2)
        if password1 == password2:
            user = User(user_type=user_type, username=username, mobile_number=mobile_number, email=email, password=encrypted_password)
            user.save()
            auth_login(request, user)
            messages.success(request, "You are register as %s successfully!" % user.get_user_type_display())
            if user.user_type:
                return redirect('dashboard_add_listing')
            return redirect('login')
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        # Get the username and password from the request.POST dictionary
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user with the provided username and password
        user = authenticate(request, username=username, password=password)
        print(user.user_type)

        if user is not None:
            # If authentication is successful, log the user in and redirect to home page
            auth_login(request, user)
            if user.user_type:
                return redirect('dashboard_add_listing')
            return redirect('index')
    else:
        # If the request method is GET, display the login form
        return render(request, 'index.html')
    

def logout_view(request):
    logout(request)
    return redirect('index')



def index(request):
    properties = Property.objects.all()
    return render(request, 'index.html',{
        'properties': properties,
    })


def dashboard_add_listing(request):
    return render(request, 'dashboard-add-listing.html')


def contacts(request):
    return render(request, 'contacts.html')


def about(request):
    return render(request, 'about.html')


def pg_Coliving(request):
    pg = LatestPg.objects.all()
    return render(request, 'pgColiving.html', {
        'pg' : pg,
    })


def plot(request):
    return render(request, 'plot.html')


def commercial(request):
    return render(request, 'commercial.html',{
    })


def rent(request):
    rent = LatesFlat.objects.all()
    return render(request, 'rent.html',{
        'rent':rent
    })


def dashboard_mypropfile(request):
    return render(request, 'dashboard-myprofile.html')


def property(request):
    return render(request, 'property.html')


def pgDetails(request):
    return render(request, 'pgDetails.html')


def rent_All_Listing(request):
    return render(request, 'rentAllListing.html')


def sell_All_Listing(request):
    return render(request, 'sellAllListing.html')


def plot_All_Listing(request):
    return render(request, 'plotAllListing.html')


def commercial_Sale_All_Listing(request):
    return render(request, 'commercialSaleAllListing.html')


def commercial_Rent_All_Listing(request):
    return render(request, 'commercialRentAllListing.html')


def pg_All_Listing(request):
    return render(request, 'pgAllListing.html')


def rent_Single_Listing(request):
    return render(request, 'rentSingleListing.html')

