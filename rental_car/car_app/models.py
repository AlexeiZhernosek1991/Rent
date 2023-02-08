from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = "Категория автомобиля"
        verbose_name_plural = "Категории автомобилей"
        ordering = ['name']


class Color(models.Model):
    color = models.CharField(max_length=200, verbose_name="Цвет")

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


class Body_type(models.Model):
    body_type = models.CharField(max_length=200, verbose_name="Тип кузова")

    def __str__(self):
        return self.body_type

    class Meta:
        verbose_name = "Тип кузова"
        verbose_name_plural = "Типы кузова"


class Type_fuel(models.Model):
    type_fuel = models.CharField(max_length=200, verbose_name="Тип топлива")

    def __str__(self):
        return self.type_fuel

    class Meta:
        verbose_name = "Тип топлива"
        verbose_name_plural = "Типы топлива"


class Transmission(models.Model):
    transmission = models.CharField(max_length=200, verbose_name="Тип топлива")

    def __str__(self):
        return self.transmission

    class Meta:
        verbose_name = "Коробка передач"
        verbose_name_plural = "Коробки передач"


class Car(models.Model):
    car_model = models.CharField(max_length=200, blank=True, verbose_name="Модель")
    register_num = models.CharField(max_length=200, blank=True, verbose_name="Регистрационный знак")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    color = models.ManyToManyField('Color', blank=True, verbose_name="Цвет")
    body_type = models.ForeignKey('Body_type', on_delete=models.PROTECT, blank=True, verbose_name="Тип кузова")
    places = models.IntegerField(blank=True, verbose_name="Количество мест")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    price_one_five = models.FloatField(blank=True, verbose_name="Цена от 1 до 5 дней")
    price_five_ten = models.FloatField(blank=True, verbose_name="Цена от 5 до 10 дней")
    price_ten = models.FloatField(blank=True, verbose_name="Цена от 10 ")
    video_review = models.URLField(max_length=500, blank=True, verbose_name="Обзор автомобиля")
    engine_capacity = models.FloatField(blank=True, verbose_name="Объем двигателя")
    power_engine = models.IntegerField(blank=True, verbose_name="Мощность двигателя")
    type_fuel = models.ForeignKey('Type_fuel', on_delete=models.PROTECT, blank=True, verbose_name="Тип топлива")
    transmission = models.ForeignKey('Transmission', on_delete=models.PROTECT, blank=True,
                                     verbose_name="Коробки передач")
    photo = models.ForeignKey('Photo', on_delete=models.PROTECT, blank=True, verbose_name="Фото")

    def __str__(self):
        return self.car_model

    def get_absolute_url(self):
        return reverse('car', kwargs={'car_slug': self.slug})

    class Meta:
        verbose_name = "Автомобили"
        verbose_name_plural = "Автомобили"
        ordering = ['car_model']


class Photo(models.Model):
    car_name = models.CharField(max_length=200, blank=True, verbose_name="Название авто")
    photo_start = models.ImageField(upload_to='img/car/%Y/%m/%d/', blank=True, verbose_name="Главное фото")
    photo_1 = models.ImageField(upload_to='img/car/%Y/%m/%d/', blank=True, verbose_name="Фото 1")
    photo_2 = models.ImageField(upload_to='img/car/%Y/%m/%d/', blank=True, verbose_name="Фото 2")
    photo_3 = models.ImageField(upload_to='img/car/%Y/%m/%d/', blank=True, verbose_name="Фото 3")
    photo_4 = models.ImageField(upload_to='img/car/%Y/%m/%d/', blank=True, verbose_name="Фото 4")

    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = "Фотографии машин"
        verbose_name_plural = "Фотографии машин"


class Order(models.Model):
    name = models.CharField(max_length=200, verbose_name="ФИО")
    date_star = models.IntegerField(verbose_name="Дата начала аренды")
    date_over = models.IntegerField(verbose_name="Дата завершения аренды")
    date_order = models.DateField(auto_created=True)
    day_rent = models.IntegerField(verbose_name="Количество дней аренды")
    telefon_num = models.IntegerField(verbose_name="Номер телефона")
    email = models.EmailField(blank=True, verbose_name="Email")
    price_rent = models.IntegerField(verbose_name="Стоимость аренды")
    car = models.ForeignKey('Car', on_delete=models.PROTECT, verbose_name="Автомобиль")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заказ на аренду автомобиля"
        verbose_name_plural = "Заказы на аренду автомобиля"
