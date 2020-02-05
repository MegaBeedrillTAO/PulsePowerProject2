from django.contrib import admin
from .models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'term_length', 'rate')


admin.site.register(Card, CardAdmin)
