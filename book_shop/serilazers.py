from .models import Category,Author,Book
from rest_framework import serializers




class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.full_name')
    author_status = serializers.BooleanField(source='author.status')
    category_name = serializers.CharField(source='category.name')
    class Meta:
        model = Book
        fields = ('name','description','photo','isbn','file','audio','download_count','author_name','category_name','author_status')
        
        
        
class AuthorSerializer(serializers.ModelSerializer):
    book_author = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ('full_name','book_author')

class CategorySerialazer(serializers.ModelSerializer):
    book_category = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ('name','book_category')




