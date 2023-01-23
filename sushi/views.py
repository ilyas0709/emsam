from django.shortcuts import render
from rest_framework import mixins, generics, viewsets, status, permissions
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class CategoryListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryAdminViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin,
                           mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class FoodListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodListSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FoodAdminViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin,
                       mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Food.objects.all()
    serializer_class = FoodDetailSerializers
    # permission_classes = (IsAdminUser, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PortionAdminView(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin,
                       mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    queryset = Portion.objects.all()
    serializer_class = PortionListSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)






# Create your views here.
