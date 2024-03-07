from django.urls import path, include
from rest_framework import routers
from .views import PersonViewSet
from resthome.views import get_persons, create_person, update_person, delete_person


router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/persons/', get_persons),
    path('api/persons/create/', create_person),
    path('api/persons/<int:pk>/update/', update_person),
    path('api/persons/<int:pk>/delete/', delete_person),
]


