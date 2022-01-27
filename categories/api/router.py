from rest_framework.routers import DefaultRouter

from categories.api.views import CategoryView


router_category = DefaultRouter()
router_category.register(prefix='', basename='category', viewset=CategoryView)
