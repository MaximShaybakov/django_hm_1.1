from django.contrib import admin
from django.urls import path, include

from app.views import home_view, time_view, workdir_view, summator, hello, welcome, show_list

urlpatterns = [
    path('', home_view, name='home'),
    path('current_time/', time_view, name='current_time'),
    path('workdir/', workdir_view, name='workdir'),
    path('sum/<int:a>/<int:b>/', summator, name='sum'),
    path('hello/', hello),
    path('welcome/', welcome),
    path('pagi/', show_list),
    path('admin/', admin.site.urls),
]