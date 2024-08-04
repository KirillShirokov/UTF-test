from rest_framework import viewsets

from .models import FoodCategory
from .serializers import FoodListSerializer


class FoodListViewSet(viewsets.ModelViewSet):

    queryset = FoodCategory.objects.filter(
        food__is_publish=True).prefetch_related('food')
    serializer_class = FoodListSerializer
