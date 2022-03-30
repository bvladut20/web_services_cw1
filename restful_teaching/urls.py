# restful_teaching URL Configuration


from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from teaching import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'professors', views.ProfessorViewSet)
router.register(r'modules', views.ModuleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include('teaching.urls')),
    path('register/', views.UserCreate.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]