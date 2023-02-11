from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .form import AddCommentForm
from .models import Comment

menu = [{'title': "Главная страница", 'url_name': 'start_page'},
        {'title': "Автопарк", 'url_name': 'cars'},
        {'title': "О нас", 'url_name': 'about_us'},
        {'title': "Отзывы", 'url_name': 'comment'},
        {'title': "Контакты", 'url_name': 'contacts'}
        ]


class Addcomment(CreateView, ListView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'comment/comment.html'
    success_url = reverse_lazy('comment')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Отзывы'
        context['menu'] = menu
        return context
