from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .form import *
from .models import *
from .utils import *


class StartPageListViwe(DataMixin, ListView):
    model = Car
    template_name = 'car/start_page.html'
    context_object_name = 'car'

    def get_queryset(self):
        return Car.objects.filter(pk__in=[1, 2, 3])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        contex_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(contex_def.items()))


class CarPageListViwe(DataMixin, ListView):
    model = Car
    template_name = 'car/car_list.html'
    context_object_name = 'car'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        contex_def = self.get_user_context(title='Автопарк')
        return dict(list(context.items()) + list(contex_def.items()))


class ShowCar(DataMixin, DetailView, ):
    model = Car
    template_name = 'car/car_detail.html'
    slug_url_kwarg = 'car_slug'
    success_url = reverse_lazy('order')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = AddOrderForm()
        context['form'] = form
        contex_def = self.get_user_context(title='Автомобиль')
        return dict(list(context.items()) + list(contex_def.items()))


class CarCategory(DataMixin, ListView):
    model = Car
    template_name = 'car/car_list.html'
    context_object_name = 'car'
    allow_empty = False

    def get_queryset(self):
        return Car.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Категория - ' + str(context['car'][0].category),
                                            cat_selected=context['car'][0].category_id)
        return dict(list(context.items()) + list(context_def.items()))


def order(request, slug):
    car = Car.objects.get(slug=slug)
    get_orders_all = Order.objects.filter(car=car)
    form = AddOrderForm()
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            day_rent = str(form.cleaned_data['date_over'] - form.cleaned_data['date_star'])
            day_rent = int(day_rent.split()[0])
            price_rent = car.price_one_five
            if 5 < day_rent < 11:
                price_rent = car.price_five_ten * day_rent
            elif 10 < day_rent:
                price_rent = car.price_ten * day_rent
            order = Order(
                name=request.user.username,
                date_star=form.cleaned_data['date_star'],
                date_over=form.cleaned_data['date_over'],
                day_rent=day_rent,
                price_rent=price_rent,
                telefon_num=form.cleaned_data['telefon_num'],
                address=form.cleaned_data['address'],
                car=car
            )
            order.save()
    context = {
        'car': car,
        'menu': menu,
        'form': form,
        'get_orders_all': get_orders_all
    }
    return render(request, 'car/order.html', context)


def contacts(request):
    context = {
        'menu': menu,
    }
    return render(request, 'car/contact.html', context)


def about_us(request):
    context = {
        'menu': menu,
    }
    return render(request, 'car/about.html', context)


class Register(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'car/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        contex_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(contex_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('start_page')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'car/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        contex_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(contex_def.items()))


def logout_user(request):
    logout(request)
    return redirect('login')
