from django.urls import path
from .views import Home, Delete


urlpatterns = [
    path('list', Home),
    path('delete_list/<int:id>', Delete),
]