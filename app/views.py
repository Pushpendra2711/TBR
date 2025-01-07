
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import SignupSerializer,LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
   
class UserLogin(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer=LoginSerializer(data=request.data)

        if serializer.is_valid():
            print("hello world")
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']
            print(f"{email}{password}")    
            user=authenticate(username=email,password=password)

            if user is not None:
                refresh=RefreshToken.for_user(user)
                return Response({"refresh":str(refresh),
                "access_token":str(refresh.access_token)})
            else:
                return Response({"message":"wroung creadential"})    

class UserSignup(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        """
        Handles POST requests to process form submissions.
        """
         # Pass the form data to the serializer for validation
        serializer=SignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully!'})
        else:
            return Response({'message': 'incorrect input!'})

        
class ProtectedApiView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        return Response({"message":"you are authenticated"})