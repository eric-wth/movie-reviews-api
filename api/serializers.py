from rest_framework import serializers
from .models import Movies, Reviews, Comments


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ["movie", "user", "rating", "review"]

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["movie", "user", "content", "parent", "create_at"]

class MoviesSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    class Meta:
        model = Movies
        fields = ["title", "release_year", "director", "plot", "poster_url"]