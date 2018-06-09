# api urls to enable get and post from front-end.

from rest_framework.routers import DefaultRouter

from .api import AddressViewSet

router = DefaultRouter()
router.register(r'addresses', AddressViewSet) # url for API endpoint for frontend

urlpatterns = router.urls