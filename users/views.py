from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import generics
import jwt, datetime

from .serializers import UserSerializer
from .models import User

# register function
class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# login function
class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        # first user as the email is uniqe no need to filter all objects
        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('user not found.')
        
        # password encrypted check
        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password.')
        
        # user levels check
        is_admin = user.is_admin
        is_editor = user.is_editor
        is_user = True
        
        if is_admin == True:
            roles = ['5150']
        
        if is_editor == True:
            roles = ['1984']
            
        if is_user == True:
            roles = ['2001']
            
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()        
        }
        
        accessToken = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='access', value=accessToken, httponly=True)
        response.data = {
         "access": accessToken,
         "roles": roles  
        }
         
        return response
    
# authenticated user
class AuthenticatedUser(APIView):
    def get(self, request):
        token = request.COOKIES.get('access')
        
        if not token:
            raise AuthenticationFailed('unauthenticated.')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthenticated.')
        
        user = User.objects.filter(id=payload['id']).first()
        
        return Response(UserSerializer(user).data)
    
# view all users
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)  
    
# logout user
class Logout(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('access')
        response.data = {
            'logout':'success logout'
        }
        return response