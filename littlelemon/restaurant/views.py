from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from datetime import datetime
from django.core import serializers
from .forms import BookingForm
from django.views.decorators.csrf import csrf_exempt
from .paginations import *
import json
from django.http import HttpResponse

# Create your views here.
#page views
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu':menu_data}
    return render(request, 'menu.html', {'menu':main_data})

def menu_item(request,pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''
    return render(request,'menu_item.html', {'menu_item': menu_item})


def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method =='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'book.html',context)

@csrf_exempt
def bookings(request):
    if request.method =='POST':
        data = json.load(request)
        exist = Booking.objects.filter(BookingDate=data['BookingDate']).exists()
        if exist == False:
         booking=Booking(
                name = data['name'],
                No_of_guests = data['No_of_guests'],
                BookingDate = data['BookingDate']
            )
         booking.save()
        else:
            return HttpResponse("{'error':1}",content_type = 'application/json')
    
    date = request.GET.get('date',datetime.now())

    bookings = Booking.objects.filter(BookingDate = date)
    booking_json = serializers.serialize('json', bookings)
    return HttpResponse(booking_json, content_type = 'application/json')

#api views
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class=MenuPagination

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    pagination_class=BookingPagination
    
