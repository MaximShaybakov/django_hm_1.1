import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course

# client = APIClient()

@pytest.fixture
def client():
    '''fixture for api-client'''
    return APIClient()


@pytest.fixture
def students(client):
    '''fixture for students factory'''
    response = client.get('/courses/')
    return response.json()


@pytest.fixture
def students(client):
    '''fixture for students'''
    response = client.get('/courses/')
    return response.json()


@pytest.fixture
def courses(client):
    '''fixture for students factory'''
    def courses_get(client, *args, **kwargs):
        response = client.get('/courses/')
        return response.json()
    return courses_get


@pytest.fixture
def courses_factory():
    '''fixture for create students'''
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_api(client):
    '''server response test'''
    response = client.get('/courses/')
    assert response.status_code == 200


@pytest.mark.django_db # если я верно понял не хватало этого теста
def test_get_course(client, courses, courses_factory):
    '''get 1 course test'''
    course = courses_factory(_quantity=1)
    response = client.get(f'/courses/?id={course[1].id})
    # response = client.get('/courses/1/')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['id'] == course[1].id
    assert data[0]['name'] == course[1].name


@pytest.mark.django_db
def test_get_course_by_id(client, courses, courses_factory):
    '''taking any course by id'''
    course = courses_factory(_quantity=10)
    response = client.get(f'/courses/?id={course[3].id}')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['id'] == course[3].id


@pytest.mark.django_db
def test_get_course_by_name(client, courses, courses_factory):
    '''taking any course by name'''
    course = courses_factory(_quantity=10)
    response = client.get(f'/courses/?name={course[3].name}')
    data = response.json()
    assert response.status_code == 200
    assert course[3].name == data[0]['name']


@pytest.mark.django_db
def test_create_course(client, courses, courses_factory):
    '''course creation test'''
    course = courses_factory(_quantity=10)
    response = client.get('/courses/')
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, (list, ))
    assert len(course) == len(courses(client))


@pytest.mark.django_db
def test_get_list_course(client, courses, courses_factory):
    '''creating and checking a list of courses'''
    course = courses_factory(_quantity=10)
    response = client.get('/courses/')
    data = response.json()
    assert response.status_code == 200
    assert len(course) == len(data)
    assert isinstance(data, (list, ))
    for index, course_ in enumerate(data):
        assert course[index].name == course_['name']


@pytest.mark.django_db
def test_create_one_course(client):
    '''create new course test'''
    response = client.post('/courses/', data={'name': 'music', 'students': []})
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, courses_factory):
    '''course update test'''
    name = 'music'
    course = courses_factory(_quantity=10)
    response = client.patch(f'/courses/{course[3].id}/', data={'name': name, 'students': []})
    new_name = client.get(f'/courses/{course[3].id}/').json()
    assert response.status_code == 200
    assert new_name['name'] == name


@pytest.mark.django_db
def test_rm_course(client, courses, courses_factory):
    '''course deletion test'''
    course = courses_factory(_quantity=10)
    response = client.delete(f'/courses/{course[3].id}/')
    new_count_courses = client.get('/courses/').json()
    response2 = client.delete(f'/courses/{course[3].id}/')
    assert response.status_code == 204
    assert response2.status_code == 404
    for _ in new_count_courses:
        assert course[3].id != _['id']
    assert len(new_count_courses) == len(course) - 1


