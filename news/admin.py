from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('username', 'title', 'published_date')
    search_fields = ('title', 'username')
    list_filter = ('published_date',)
