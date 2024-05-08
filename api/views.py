from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movies, Reviews, Comments
from .serializers import MoviesSerializer, ReviewsSerializer, CommentsSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle


class MoviesApiView(APIView):    
    #returns all the movies
    def get(self, request):
        movies = Movies.objects.all()
        serializer = MoviesSerializer(movies, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    
    #users can create a movie
    def post(self, request):
        data = {
            'title': request.data.get('title'),
            'release_year': request.data.get('release_year'),
            'director': request.data.get('director'),
            'plot': request.data.get('plot'),
        }

        serializer = MoviesSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class MoviesDetailApiView(APIView):
    #helper method to get an object given the movie_id
    def get_object(self, movie_id):
        try:
            return Movies.objects.get(id = movie_id)
        except Movies.DoesNotExist:
            return None

    #retrieve movie object given movie_id
    def get(self, request, movie_id):
        movie_instance = self.get_object(movie_id)

        if not movie_instance:
            return Response(
                {"res": "Object with movie id does not exist"},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer = MoviesSerializer(movie_instance)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    
    #update a movie object given movie_id
    def put(self, request, movie_id):
        movie_instance = self.get_object(movie_id)

        if not movie_instance:
            return Response(
                {"res": "Object with movie id does not exist"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'title': request.data.get('title'),
            'release_year': request.data.get('release_year'),
            'director': request.data.get('director'),
            'plot': request.data.get('plot')
        }
        
        serializer = MoviesSerializer(instance = movie_instance, data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

    #delete a movie object given movie_id
    def delete(self, request, movie_id):
        movie_instance = self.get_object(movie_id)

        if not movie_instance:
            return Response(
                {"res": "Object with movie id does not exist"},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        movie_instance.delete()
        
        return Response(
            {"res": "Object deleted!"},
            status = status.HTTP_200_OK
        )
    

class ReviewAPIView(APIView):
    #allows users to post a review
    def post(self, request):
        #get user id and movie id from Request object
        user_id = request.data.get('user')
        movie_id = request.data.get('movie')

        #get review data from the Request object
        review_data = request.data.get('review')

        #add user id and movie id to the review data
        review_data['user'] = user_id
        review_data['movie'] = movie_id

        #serialize data and save it
        review_serializer = ReviewsSerializer(data = review_data)

        if review_serializer.is_valid():
            review_serializer.save()
            return Response(review_serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(review_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

class ReviewDetailAPIView(APIView):
    throttle_class = [UserRateThrottle]
    pagination_class = PageNumberPagination


    #allows users to get reviews
    def get(self, request, movie_id):
        review_instances = Reviews.objects.filter(movie = movie_id)

        serializer = ReviewsSerializer(review_instances, many = True)

        return Response(serializer.data, status = status.HTTP_200_OK)
    
class CommentDetailAPIView(APIView):
    def get(self, request):
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
