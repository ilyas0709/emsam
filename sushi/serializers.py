from rest_framework import serializers
from .models import *


class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()


class CategoryDetailSerializers(serializers.ModelSerializer):
    food = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = 'id name food'.split()


class FoodListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = 'id category name image composition portion'.split()


class FoodDetailSerializers(serializers.ModelSerializer):
    portion = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Food
        fields = 'id category name image composition portion'.split()


class PortionListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Portion
        fields = 'id food price_size30 size36'.split()
#
#
# class PortionDetailSerializers(serializers.ModelSerializer):
#
#     class Meta:
#         model = Portion
#         fields = '__all__'.split()

