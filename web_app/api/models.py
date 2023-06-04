from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Coin(models.Model):
    code = models.TextField(
        max_length=50,
        verbose_name='Символьный код',
    )
    name = models.TextField(
        max_length=50,
        verbose_name='Наименование монеты',
    )
    price = models.FloatField(
        verbose_name='Текущий курс'
    )
    timestamp = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего обновления',
    )
    total_supply = models.IntegerField(
        verbose_name='Объем торгов'
    )
    percent_change = models.FloatField(
        verbose_name='% изменения'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class News(models.Model):
    author = models.TextField(
        max_length=256,
        verbose_name='Автор публикации',
    )
    description = models.TextField(
        verbose_name='Текст публикации',
    )
    title = models.TextField(
        max_length=256,
        verbose_name='Заголовок публикации',
    )
    published = models.DateField(
        db_index=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        ordering = ['published']

    def __str__(self):
        return self.author
