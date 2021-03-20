from rest_framework import serializers
from main.models import Book, Journal


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'price',
            'num_pages',
            'genre',
            'description',
            'created_at'
        )
        model = Book

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'price',
            'num_pages',
            'type',
            'publisher',
            'created_at'
        )
        model = Journal