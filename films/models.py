from django.db import models


class Film(models.Model):
    title = models.CharField("Название фильма", max_length=200)
    description = models.TextField("Описание фильма", blank=True)
    review = models.TextField("Отзыв", blank=True)
    image = models.ImageField("Постер", upload_to='films/', blank=True, null=True)  # ← Новое поле
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
