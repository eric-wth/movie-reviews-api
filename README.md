# Movie Reviews API
The Movies Review API is a RESTful web service designed to facilitate the management and retrieval of movie reviews. This project enables users to register, log in securely, add movies to the database, and contribute reviews for those movies. By providing a simple yet powerful API, developers can integrate movie review functionality into various applications, such as movie databases or social media platforms.

## Features
User Authentication: Users can sign up for an account or log in using their existing credentials.

Movie Management: Authorized users can add new movies to the database by providing details such as title, release year, genre, director, and cast. Movies can also be updated or deleted as needed.
Users can browse a collection of movies, view details about each movie, and read reviews written by other users.

Write Reviews: Authenticated users can write and submit reviews for movies they have watched.

View User Reviews: Users can see all the reviews they have written.

Rate Limiting: API endpoints are protected with rate limiting to prevent abuse and ensure fair usage.

Pagination: Results are paginated to improve performance and provide a better user experience.

## Technologies Used
Backend Framework: Python with Django for building the RESTful API endpoints.

Database: SQLite for storing movie and review data.

Authentication: Token-based user authentication and authorization

## Installation
To run the Movie Review App locally, follow these steps:

Clone the repository to your local machine:

``` bash
Copy code
git clone https://github.com/yourusername/movie-review-app.git
```

Navigate to the project directory:
```bash
cd movie-review-app
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

Set up the database:
```bash
python manage.py migrate
```

Create a superuser account (optional):
```bash
python manage.py createsuperuser
```

Start the development server:
```bash
python manage.py runserver
```

Access the app in your web browser at http://localhost:8000.

## Usage
Register for a new account or log in with existing credentials.
Browse the list of movies and click on a movie to view its details and reviews.
Write your own review for a movie by clicking the "Write a Review" button.
View all the reviews you have written by navigating to the "My Reviews" section.
Enjoy discovering and reviewing movies with the Movie Review App!