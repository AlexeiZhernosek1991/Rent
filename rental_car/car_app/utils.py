from .models import Category

menu = [{'title': "Главная страница", 'url_name': 'start_page'},
        {'title': "Автопарк", 'url_name': 'cars'},
        {'title': "О нас", 'url_name': 'about_us'},
        {'title': "Отзывы", 'url_name': 'comment'},
        {'title': "Контакты", 'url_name': 'contacts'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        # user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(1)
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context



