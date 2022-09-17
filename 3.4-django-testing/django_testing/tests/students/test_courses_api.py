import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course

# client = APIClient()

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def students(client):
    response = client.get('/courses/')
    return response.json()


@pytest.fixture
def courses(client):
    def courses_get(client, *args, **kwargs):
        response = client.get('/courses/')
        return response.json()
    return courses_get


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_api(client):
    response = client.get('/courses/')
    assert response.status_code == 200


@pytest.mark.django_db # проверка получения 1го курса (retrieve-логика)
def test_get_course(client, courses, courses_factory):
    course = courses_factory(_quantity=1)
    response = client.get('/courses/1/')
    assert course[0].name == response.json()['name']
    assert course[0].id == 1


@pytest.mark.django_db
def test_create_course(client, courses, courses_factory):
    course = courses_factory(_quantity=10)
    response = client.get('/courses/')
    assert len(course) == len(courses(client))


@pytest.mark.django_db
def test_get_list_course(client, courses, courses_factory):
    course = courses_factory(_quantity=10)
    response = client.get('/courses/')
    for index, course_ in response:
        assert course_.json()[index]['name'] == course[index].name


@pytest.mark.django_db
def test_create_one_course(client):
    response = client.post('/courses/', data={'name': 'music', 'students': []})
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, courses, courses_factory):
    course = courses_factory(_quantity=1)
    response = client.patch('/courses/', data={'name': 'music', 'students': []})
    assert response.status_code == 201


@pytest.mark.django_db
def test_rm_course(client, courses, courses_factory):
    course = courses_factory(_quantity=1)
    response = client.delete('/courses/1/')
    assert response.status_code == 204


