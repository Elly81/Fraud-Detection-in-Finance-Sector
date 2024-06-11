from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_fraud, name='predict_fraud'),  # This matches 'predict/' path
]
