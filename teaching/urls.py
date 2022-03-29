from django.urls import path

from . import views

urlpatterns = [
    path('ratings/', views.RatingViewSet.as_view({'get': 'all_ratings_list'})),
    path('ratings/<module_id>/<professor_id>/', views.RatingViewSet.as_view({'get': 'filtered_rating_list'})),
    #path('ratings/<int:module_id>/<int:professor_id>', views.RatingViewSet.as_view({'get': 'list'})),
    path('ratings/<int:module_id>/<int:professor_id>/avg', views.RatingViewSet.as_view({'get': 'average_rating'})),
    path('ratings/add/', views.RatingCreate.as_view())
]