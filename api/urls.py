from django.urls import path
from .views import (
    MoviesApiView,
    MoviesDetailApiView,
    ReviewAPIView,
    ReviewDetailAPIView,
    CommentDetailAPIView
)

urlpatterns = [
    path('movies/', MoviesApiView.as_view()),
    path('movie/<int:movie_id>/', MoviesDetailApiView.as_view()),
    path('reviews/', ReviewAPIView.as_view()),
    path('reviews/<int:movie_id>', ReviewDetailAPIView.as_view()),
    path('comments/', CommentDetailAPIView.as_view())
]