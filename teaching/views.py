from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from .serializers import UserSerializer, GroupSerializer, ProfessorSerializer, ModuleSerializer, RatingSerializer
from teaching.models import Professor, Module, Rating
from django.http import JsonResponse


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class RatingCreate(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


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
    permission_classes = (IsAuthenticated,)


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = (IsAuthenticated,)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def filtered_rating_list(self, request, *args, **kwargs):
        if request.method == 'GET':
            queryset = self.queryset
            module_choice = self.kwargs['module_id']
            professor_choice = self.kwargs['professor_id']
            if module_choice is not None and professor_choice is not None:
                queryset = queryset.filter(module_id__exact=module_choice, professor_id__exact=professor_choice)
                serializer = RatingSerializer(queryset, many=True)
                return JsonResponse(serializer.data, safe=False)

    @action(detail=False, methods=['get'])
    def all_ratings_list(self, request):
        if request.method == 'GET':
            queryset = self.queryset
            serializer = RatingSerializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)

    @action(detail=False, methods=['get'])
    def average_rating(self, request, *args, **kwargs):
        if request.method == 'GET':
            queryset = self.queryset
            module_choice = self.kwargs['module_id']
            professor_choice = self.kwargs['professor_id']
            if module_choice is not None and professor_choice is not None:
                queryset = queryset.filter(module_id__exact=module_choice, professor_id__exact=professor_choice)
                serializer = RatingSerializer(queryset, many=True)
                new_data = 0.0
                divisor = 0
                for data in serializer.data:
                    professor_check = 0
                    module_check = 0
                    rating_value = 0.0
                    for key, value in data.items():
                        if key == "value":
                            rating_value = value
                        if key == "professor":
                            if value == professor_choice:
                                professor_check = 1
                        if key == "module":
                            if value == module_choice:
                                module_check = 1
                        if professor_check == 1 and module_check == 1:
                            new_data = new_data + rating_value
                            divisor = divisor + 1

                new_data = new_data / divisor
                new_data = round(new_data, 2)
                return JsonResponse(new_data, safe=False)

