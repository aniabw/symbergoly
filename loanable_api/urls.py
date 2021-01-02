from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
# from users import views as user_views
from applications import views as application_views

router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'users', user_views.UserViewSet)
# router.register(r'groups', user_views.GroupViewSet)
router.register(r'newapplications', application_views.ApplicationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]