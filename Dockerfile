#base image
FROM python:3.6

#environment variable
ENV PYTHONUNBUFFERED 1

#root directory for the project in the container
RUN mkdir /movie_reviews_service

#working directory
WORKDIR /movie_reviews_service

#copy current directory contents into working directory
COPY . /movie_reviews_service/

#install required packages
RUN pip install -r requirements.txt