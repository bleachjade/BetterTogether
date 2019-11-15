from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django import forms
from datetime import datetime

myDate = datetime.now()
formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")

def index(request):
    return render(request, 'BetterTogetherApp/homepage.html')

def share_ride_index(request):
    share_ride = ShareRide.objects.all()
    context = {'share_ride' : share_ride, 'datetime' : formatedDate }
    return render(request, 'BetterTogetherApp/share_ride_index.html', context)

def share_promotion_index(request):
    share_promotion = SharePromotion.objects.all()
    context = {'share_promotion' : share_promotion, 'datetime' : formatedDate }
    return render(request, 'BetterTogetherApp/share_promotion_index.html', context)

# def share_food_index(request):
#     share_food = ShareFood.objects.all()
#     context = {'share_food' : share_food}
#     return render(request, 'BetterTogetherApp/index.html', context)


def user_profile(request, user_id):
    pass

def create_share_food(request):
    pass


def create_share_promotion(request):
    form = SharePromotionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            location_name = form.data.get('location_name')
            location = form.data.get('location')
            brand = form.data.get('brand')
            description = form.data.get('description')
            date = form.data.get('day')
            time = form.data.get('time')
            num_people = form.data.get('num_people')
            sp = SharePromotion(location_name=location_name,location=location, brand=brand, 
            description=description, date_time=(str(f"{date} {time}")), num_people=num_people)   
            sp.save()
            return redirect('BetterTogetherApp:share_promotion_index1')

    context = {'form': form, 'date_time': DateForm}
    return render(request, 'BetterTogetherApp/share_promotion_create.html', context)

def delete_share_promotion(request, sharepromo_id):
    share = SharePromotion.objects.get(pk=sharepromo_id)
    share.delete()
    return redirect('BetterTogetherApp:share_promotion_index1')

def create_share_ride(request):
    form = ShareRideForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            location_name = form.data.get('location_name')
            location = form.data.get('location')
            destination_name = form.data.get('destination_name')
            destination = form.data.get('destination')
            description = form.data.get('description')
            date = form.data.get('day')
            time = form.data.get('time')
            num_people = form.data.get('num_people')
            sr = ShareRide(location_name=location_name,location=location, destination_name=destination_name,destination=destination,
             description=description, date_time=(str(f"{date} {time}")), num_people=num_people)   
            sr.save()
            return redirect('BetterTogetherApp:share_ride_index1')

    context = {'form': form, 'date_time': DateForm}
    return render(request, 'BetterTogetherApp/share_ride_create.html', context)

def delete_share_ride(request, shareride_id):
    shareride1 = ShareRide.objects.get(pk=shareride_id)
    shareride1.delete()
    return redirect('BetterTogetherApp:share_ride_index1')