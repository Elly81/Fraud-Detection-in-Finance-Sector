from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('predict/', include('myapp.urls')),  # Include the URL configuration of your app
    path('', RedirectView.as_view(url='/predict/', permanent=True)),  # Redirect the root URL to /predict/
]
