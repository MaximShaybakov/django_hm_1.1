import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student():
    return Student.objects.create('admin')

@pytest.fixture
def students():
    return Student.objects.all()

@pytest.mark.django_db
def test_create_students():
    
    
    # data = response.json()
    # assert len(data) == 1