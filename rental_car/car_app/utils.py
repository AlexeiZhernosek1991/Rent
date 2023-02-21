from .models import Category, Type_fuel, Transmission

menu = [{'title': "Главная страница", 'url_name': 'start_page'},
        {'title': "Автопарк", 'url_name': 'cars'},
        {'title': "Контакты", 'url_name': 'contacts'},
        {'title': "Отзывы", 'url_name': 'comment'},
        {'title': "Наши партнеры", 'url_name': 'partner'},
        ]


def get_cats():
    cats = Category.objects.all()
    return cats


def get_fuel():
    fuel = Type_fuel.objects.all()
    return fuel


def get_transmission():
    trans = Transmission.objects.all()
    return trans


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['cats'] = get_cats()
        context['fuel'] = get_fuel()
        context['trans'] = get_transmission()
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
