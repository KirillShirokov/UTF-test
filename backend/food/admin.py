from django.contrib import admin

from food.models import FoodCategory, Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'is_vegan',
        'code',
        'internal_code',
        'name_ru',
        'description_ru',
        'cost',
        'is_publish',
    )
    list_display_links = (
        'id',
    )
    search_fields = (
        'id',
    )
    list_filter = (
        'id',
    )


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_ru',
        'name_en',
        'name_ch',
        'order_id',
    )
    list_display_links = (
        'id',
    )
    search_fields = (
        'id',
    )
    list_filter = (
        'id',
    )
