from django.urls import path
from .views import home_view, redirect_url_view

urlpatterns = [
    path('', home_view, name='home'),
    path('<str:short_url>', redirect_url_view, name='redirect')
]
