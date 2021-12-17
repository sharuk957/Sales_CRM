from rest_framework.authentication import get_authorization_header,BaseAuthentication

from rest_framework import exceptions
import jwt

from .models import Users

class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        

        auth_header = get_authorization_header(request)

        auth_data  = auth_header.decode('utf-8')

        auth_token = auth_data.split(" ")

        if len(auth_token)!=2:
            raise exceptions.AuthenticationFailed('invalid token')

        token = auth_token[1]

        try:

            payload = jwt.decode(token,'secret',algorithms='HS256')

            user_id = payload['id']

            user = Users.objects.get(id=user_id)

            return (user,token)

        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed('token expired')
        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed('token expired')
        except Users.DoesNotExist as ex:
            raise exceptions.AuthenticationFailed("user is not found")

        
