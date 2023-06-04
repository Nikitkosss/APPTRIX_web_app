from django.contrib import admin

from api.models import Coin, News


@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'description', 'title', 'published')
    search_fields = ('title',)
    list_filter = ('published',)
    empty_value_display = '-пусто-'


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'code',
                    'name',
                    'price',
                    'timestamp',
                    'total_supply',
                    'percent_change'
                    )
    search_fields = ('code', 'name')
    list_filter = ('timestamp',)
    empty_value_display = '-пусто-'
