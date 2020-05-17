from .models import Client, Room
from .serializers import ClientSerializer, RoomSerializer
from rest_framework import viewsets
from .permissions import ReadOnly, IsSuperUser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication


class ClientViewSet(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperUser]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
