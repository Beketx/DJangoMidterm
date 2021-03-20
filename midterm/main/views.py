from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer


class BookViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    queryset = Book.objects.all()
    serializer = BookSerializer

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(user)
        return Response(serializer.data)

    # def destroy(self,request, pk=None):
    #     queryset = Book.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     user.is_active = False
    #     user.save()
    #     return Response(data='Deleting successful')

    def update(self, request, pk=None):
        print(request.data['result'])

    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def perform_destroy(self, user):
        user.delete()

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)

class JournalViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    queryset = Journal.objects.all()
    serializer = JournalSerializer

    def list(self, request):
        queryset = Journal.objects.all()
        serializer = JournalSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Journal.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = JournalSerializer(user)
        return Response(serializer.data)

    # def destroy(self,request, pk=None):
    #     queryset = Book.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     user.is_active = False
    #     user.save()
    #     return Response(data='Deleting successful')

    def update(self, request, pk=None):
        print(request.data['result'])

    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def perform_destroy(self, user):
        user.delete()

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)



