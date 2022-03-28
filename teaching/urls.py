from django.urls import path

from . import views

urlpatterns = [
    path('ratings/<int:module_id>/<int:professor_id>', views.RatingViewSet.as_view({'get': 'list'})),
]