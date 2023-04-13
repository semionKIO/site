from django.urls import path
from . import views

urlpatterns = [
    path('', views.db_home, name='db_home'),
    path('<int:pk>', views.Detail_home.as_view(), name = 'home_detail'),
    path('coment/', views.coment, name = 'coment'),
    path('add_coment/', views.add_coment, name = 'add_coment'),
    path('test/', views.index, name = 'test')
]
