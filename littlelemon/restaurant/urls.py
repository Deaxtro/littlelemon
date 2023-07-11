from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tables', BookingViewSet,basename='bookingapi')

urlpatterns = [
    #page urls
    path('', home, name="home"),
    path('restaurant/about/', about, name="about"),
    path('restaurant/menu/', menu, name ='menu'),
    path('restaurant/menu/<int:pk>',menu_item,name='menu_item'),
    path('restaurant/book/', book, name="book"),
    path('restaurant/reservations/', reservations, name="reservations"),
    #api view urls
    path('restaurant/api/menu/', MenuItemView.as_view(),name='menu_api'),
    path('restaurant/api/menu/<int:pk>', SingleMenuItemView.as_view()),
    path('restaurant/api/booking/', include(router.urls),),
    path('restaurant/bookings/', bookings, name='bookings'),
]