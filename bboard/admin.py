from django.contrib import admin

# Register your models here.
from .models import Phone

admin.site.register(Phone)

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}