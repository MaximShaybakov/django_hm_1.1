from django.urls import path
from calculator.views import home_view, recipes


urlpatterns = [
    # здесь зарегистрируйте вашу view-функцию
    path('', home_view, name='home'),
    path('<str:name_dish>/', recipes, name='recipes')
]
