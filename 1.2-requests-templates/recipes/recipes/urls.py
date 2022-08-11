from django.urls import path
from calculator.views import home_view, recipes


urlpatterns = [
    path('<str:recipe>/', recipes, name='recipes')
]
