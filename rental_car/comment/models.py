from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    comment = models.TextField(verbose_name="Отзыв")
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(verbose_name="Email")
    photo = models.ImageField(upload_to=f'img/comment/%Y/%m/%d/', blank=True, verbose_name="Фото")
    processed_or_not = models.BooleanField(default=False, verbose_name="Обработан отзыв")
    answer = models.TextField(blank=True, verbose_name="Ответ на отзыв")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-date']
