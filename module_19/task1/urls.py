from django.urls import path
from task1.views import index, games, cart, registration, new_func
urlpatterns = [
    path('', index),
    path('games/', games),
    path('cart/', cart),
    path('registration/', registration),
    path('news/', new_func),
]