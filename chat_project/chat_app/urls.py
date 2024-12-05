from django.urls import path
from . views import *

urlpatterns = [
    path('chat/<str:recipient_username>/', chat_view, name='chat'),
    path('', register_view, name='register'),
    path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
]
