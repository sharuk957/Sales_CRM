from rest_framework.serializers import ModelSerializer
from .models import Product,Person

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'
