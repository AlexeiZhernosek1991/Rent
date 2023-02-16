from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .form import AddCommentForm
from .models import Comment
from car_app.utils import get_cats, menu, DataMixin


class Addcomment(DataMixin, CreateView, ListView):
    paginate_by = 3
    model = Comment
    form_class = AddCommentForm
    template_name = 'comment/comment.html'
    success_url = reverse_lazy('comment')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        contex_def = self.get_user_context(title='Отзывы')
        return dict(list(context.items()) + list(contex_def.items()))

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)
