from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Customer, Restaurant
# Create your views here.

def index(request):
    return render(request, 'delivery/index.html')

def open_signin(request):
    return render(request, 'delivery/signin.html')

def open_signup(request):
    return render(request, 'delivery/signup.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        # if (Customer.objects.filter(username = username).exists()):
        #     return HttpResponse("Username already exits")

        try:
            Customer.objects.get(username = username)
            return HttpResponse("Duplicate username!")
        except:
            Customer.objects.create(
            username = username,
            password = password,
            email = email,
            mobile = mobile,
            address = address,
        )

            
        
    return render(request, 'delivery/signin.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

    try:
        Customer.objects.get(
            username = username,
            password = password
        )
        if username == 'admin':
            return render(request, 'delivery/admin_home.html')
        else:
            return render(request, 'delivery/customer_home.html')

    except Customer.DoesNotExist:
        return render(request, 'delivery/fail.html')



def open_add_restaurant(request):
    return render(request, 'delivery/add_restaurant.html')

def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')

        try:
            Restaurant.objects.get(name = name)
            return HttpResponse('Duplicate Restaurant')
        except:
            Restaurant.objects.create(
                name = name,
                picture = picture,
                cuisine = cuisine,
                rating = rating,
            )
    
    return render(request, 'delivery/admin_home.html')



def open_show_restaurant(request):
    restaurantList = Restaurant.objects.all()
    return render(request, 'delivery/show_restaurant.html', {'restaurantList': restaurantList})