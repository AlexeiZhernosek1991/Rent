from django.urls import path
from .views import *

urlpatterns = [
    path('', StartPageListViwe.as_view(), name='start_page'),
    path('cars/', CarPageListViwe.as_view(), name='cars'),
    path('car/<slug:car_slug>/', ShowCar.as_view(), name='car'),
    path('category/<slug:category_slug>/', CarCategory.as_view(), name='category'),
    path('partner/', partner, name='partner'),
    path('order/<slug:slug>', order, name='order'),
    path('order_finish/', order_finish, name='order_finish'),
    path('contacts/', contacts, name='contacts'),
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]
