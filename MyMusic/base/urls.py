from django.urls import path

from MyMusic.base.views import home_page

urlpatterns = [
    path('', home_page, name='home-page')
]
