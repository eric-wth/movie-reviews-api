from rest_framework import serializers
from .models import Movies, Reviews

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ["title", "release_year", "director", "plot", "poster_url"]


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ["movie", "user", "rating", "review"]