from django.shortcuts import render, get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import (
    viewsets, 
    views, 
    permissions, 
    mixins, 
    generics, 
    authentication,
)
from rest_framework.response import Response
from api.models import CustomUser, Condition, Prescription
from api.serializers import UserSerializer, ConditionSerializer, PrescriptionSerializer
from api.permissions import IsOwner


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]   

class CustomAuthToken(ObtainAuthToken):   
    # return more info when getting user token
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email
        })

class PrescriptionView(viewsets.ModelViewSet):
    """ api/drugs/"""
    queryset = Prescription.objects.all().order_by("-pk")
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PrescriptionSerializer

class UserPrescriptionList(generics.ListCreateAPIView):
    """
    api/user/:user_id/drugs/ (GET) (POST)
    create and list user prescriptions
    """
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = PrescriptionSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Prescription.objects.filter(user=user_id).order_by("-pk")

class UserPrescriptionDetail(generics.RetrieveDestroyAPIView):
    """
    api/user/:user_id/drugs/:prescription_id (GET) (DELETE)
    view and delete user prescriptions 
    """
    model = Prescription
    serializer_class = PrescriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    # self.check_object_permissions(request, obj)

    def get_queryset(self):
        user = get_object_or_404(CustomUser, pk=self.kwargs.get("user_id"))
        prescription = get_object_or_404(Prescription, pk=self.kwargs.get('pk'), user=user.pk)
        return prescription

