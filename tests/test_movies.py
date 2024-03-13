import pytest
from rest_framework.test import APIClient
from api.models import Movies

client = APIClient()

@pytest.mark.django_db
def test_get_movie():
    response = client.get('/api/movies/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_movie():
    payload = dict(
        title = 'bnds',
        release_year = 1990,
        director = 'Me',
        plot = 'shaghala baghala'

    )

    response = client.post('/api/movies/', payload)
    data = response.data
    
    assert data['title'] == payload['title']
    assert data['release_year'] == payload['release_year']
    assert data['director'] == payload['director']
    assert data['plot'] == payload['plot']


@pytest.mark.django_db
def test_get_particular_movie():
    #create movie in order to retrieve it
    payload = dict(
        title = 'bnds',
        release_year = 1990,
        director = 'Me',
        plot = 'shaghala baghala'

    )

    response = client.post('/api/movies/', payload)

    response = client.get(f'/api/movie/1/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_movie():
    #create movie record in order to update it
    payload = dict(
        title = 'bnds',
        release_year = 1990,
        director = 'Me',
        plot = 'shaghala baghala'

    )
    response = client.post('/api/movies/', payload)

    #define update payload
    update_payload = dict(
        title = 'bnds',
        release_year = 1993,
        director = 'Me & Myself',
        plot = 'shaghala baghala and more'
    )

    #update record using the REST API
    response = client.put(f'/api/movie/1/', update_payload)

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_movie():
    #create movie record in order to delete it
    payload = dict(
        title = 'bnds',
        release_year = 1990,
        director = 'Me',
        plot = 'shaghala baghala'

    )
    response = client.post('/api/movies/', payload)

    response = client.delete(f'/api/movie/1/')
    
    assert response.status_code == 200

