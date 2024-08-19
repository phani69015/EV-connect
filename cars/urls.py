from django.urls import path
from . import views

urlpatterns = [
    # Other paths...
    path('', views.home, name='home'), 
    path('find-my-ev/', views.find_my_ev, name='find_my_ev'),
    path('predict_my_ev/', views.predict_my_ev, name='predict_my_ev'),
]
