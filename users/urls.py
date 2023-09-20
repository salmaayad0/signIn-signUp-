from django.urls import path
from .views import *

urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('user', AuthenticatedUser.as_view()),
    path('logout', Logout.as_view()),
    path('users', UserList.as_view(queryset=User.objects.all(), 
                                   serializer_class=UserSerializer), name='user-list'),    
]
