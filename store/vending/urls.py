from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/
    path('cats/<int:cat_id>/', categories, name='categories'),  # http://127.0.0.1:8000/cats/
]
