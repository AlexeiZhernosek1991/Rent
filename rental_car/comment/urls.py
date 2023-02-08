from django.urls import path
from .views import Addcomment

urlpatterns = [
    path('', Addcomment.as_view(), name='comment'),
]
