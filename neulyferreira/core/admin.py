from django.contrib import admin
from .models import Post
from .models import Category


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author','created_at']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('category', 'title')}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ['title', 'slug']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
