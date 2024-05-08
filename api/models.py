from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length = 255)
    release_year = models.IntegerField(null = True, blank = True)
    director = models.CharField(max_length = 255, null = True, blank = True)
    plot = models.TextField(null = True, blank = True)
    poster_url = models.CharField(max_length = 255, null = True, blank = True)

    def __str__(self):
        return self.title
    
class Genres(models.Model):
    genre_name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.genre_name
    
class MovieGenres(models.Model):
    movie = models.ForeignKey(Movies, on_delete = models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete = models.CASCADE)

class Users(models.Model):
    username = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)
    password_hash = models.CharField(max_length = 255)
    registration_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.username
    
class Reviews(models.Model):
    movie = models.ForeignKey(Movies, on_delete = models.CASCADE)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    rating = models. DecimalField(max_digits = 3, decimal_places = 1)
    review = models.TextField()
    review_date = models.DateTimeField(auto_now_add = True)

class Favourites(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete = models.CASCADE) 

class Comments(models.Model):
    movie = models.ForeignKey(Movies, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
