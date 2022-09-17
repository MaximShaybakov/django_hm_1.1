import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course

# client = APIClient()

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def courses(client):
    response = client.get('/courses/')
    return response.json()


@pytest.mark.django_db
def test_api(client):
    response = client.get('/courses/')
    assert response.status_code == 200
    
    
@pytest.mark.django_db
def test_create_course(courses, courses_factory):
    course = courses_factory(_quantity=10)
    assert len(course) == len(courses)
    
