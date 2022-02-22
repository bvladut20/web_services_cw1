from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer, GroupSerializer, ProfessorSerializer
from teaching.models import Professor, Module, Rating


def index(request):
    return HttpResponse("Hey ur at the index page now")


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

    # @action(detail=True, methods=['post'])
    # def add_user(self, request):
    #     user = self.get_object()
    #     serializer = ProfessorSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user.add_user(serializer.validated_data['username', 'password'])
    #         user.save()
    #         return Response({'status': 'added new user'})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    #permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def add_professor(self, request):
        professor = self.get_object()
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            professor.add_professor(serializer.validated_data['name'])
            professor.save()
            return Response({'status': 'added new professor'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
