from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]