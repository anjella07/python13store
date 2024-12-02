from rest_framework import serializers
from .models import Category, Product


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductSerializers(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ['id', 'product_name', 'description', 'price', 'have', 'image', 'video', 'created_date', 'category']