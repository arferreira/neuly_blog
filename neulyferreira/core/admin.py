from django.contrib import admin
from .models import Category, Ad, About, Post, Banner

# Custom admin
admin.site.site_header = 'Neuly Ferreira | Backend'
admin.site.site_url = True

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author','created_at']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('category', 'title')}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ['title', 'slug']

class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    search_fields = ['title']

class AboutAdmin(admin.ModelAdmin):
    list_display = ['summary']
    search_fields = ['summary']

class BannerAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Banner, BannerAdmin)
