from django.urls import include, path
from rest_framework import routers

from food.views import FoodListViewSet


router_v1 = routers.DefaultRouter()
router_v1.register(r'foods', FoodListViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
]
