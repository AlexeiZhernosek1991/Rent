from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
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


class AddCarOrder(DataMixin, CreateView):
    model = Order
    form_class = AddOrderForm
    template_name = 'car/order.html'
    success_url = reverse_lazy('order')

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.name = Car.objects.get(slug=self.request.slug)
        fields.day_rent = form.fields.date_over - form.fields.date_star
        if fields.day_rent < 6:
            fields.price_rent = fields.day_rent * fields.name.price_one_five
        elif 5 < fields.day_rent < 11:
            fields.price_rent = fields.day_rent * fields.name.price_five_ten
        elif 11 < fields.day_rent:
            fields.price_rent = fields.day_rent * fields.name.price_ten
        fields.save()
        return super().form_valid(form)

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заказ'
        context['menu'] = menu
        return context


def about_us(request):
    return HttpResponse("О нас")


def contacts(request):
    return HttpResponse("Контакты")
