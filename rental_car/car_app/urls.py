from django.urls import path
from .views import *

urlpatterns = [
    path('', StartPageListViwe.as_view(), name='start_page'),
    path('cars/', CarPageListViwe.as_view(), name='cars'),
    path('car/<slug:car_slug>/', ShowCar.as_view(), name='car'),
    path('category/<slug:category_slug>/', CarCategory.as_view(), name='category'),
    path('about_us/', about_us, name='about_us'),
    path('order/<slug:slug>', AddCarOrder.as_view(), name='order'),
    # path('order/', addorder, name='order')
]
