from django.contrib import admin
from .models import Category,Author,Book
# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('name',)
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('full_name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','category','author','isbn','status','created_at')
    list_filter = ('category','author','status','created_at')
    search_fields = ('name','description','author','category','isbn')