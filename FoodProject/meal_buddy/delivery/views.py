from django.shortcuts import render , get_object_or_404 # type: ignore
from django.http import HttpResponse  # type: ignore 
from .models import Customer, Restaurant, Items

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
    restaurantList = Restaurant.objects.all()
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
            return render(request, 'delivery/customer_home.html', {'restaurantList' : restaurantList , 'username' : username} )

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



def open_update_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    return render(request, 'delivery/update_restaurant.html', {'restaurant': restaurant})


# def open_update_restaurant(request):
#     return render(request, 'delivery/update_restaurant.html')

def update_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')
        
        restaurant.name = name
        restaurant.picture = picture
        restaurant.cuisine = cuisine
        restaurant.rating = rating

        restaurant.save()

    restaurantList = Restaurant.objects.all()
    return render(request, 'delivery/show_restaurant.html',{"restaurantList" : restaurantList})
        

def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id = restaurant_id)
    # restaurant = Restaurant.objects.get(id = restaurant_id)
    restaurant.delete()
    restaurantList = Restaurant.objects.all()
    return render(request, 'delivery/show_restaurant.html', {'restaurantList': restaurantList})   


def open_update_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    # itemList = Items.objects.all()
    itemList = restaurant.items.all()
    return render(request, 'delivery/update_menu.html', {'restaurant' : restaurant , 'itemList': itemList})

def update_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get( id = restaurant_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        vegeterian = request.POST.get('is_veg') == 'on'
        picture = request.POST.get('picture')
    
        try:
            Items.objects.get(name = name)
            return HttpResponse("duplicate name")
        except:
            Items.objects.create(
                restaurant = restaurant,
                name = name,
                description = description,
                price = price,
                vegeterian = vegeterian,
                picture = picture,
            )
    return render(request, 'delivery/admin_home.html')

def view_menu(request, restaurant_id, username):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    # itemList = Items.objects.all()
    itemList = restaurant.items.all()
    return render(request, 'delivery/customer_menu.html', {'restaurant' : restaurant , 'itemList': itemList, 'username': username})

def add_to_cart(request, item_id, username):
    return HttpResponse("add to card logic")