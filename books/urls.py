from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.detail, name='detail')
]
