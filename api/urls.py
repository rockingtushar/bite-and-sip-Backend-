from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, ReservationViewSet, OrderViewSet, ContactMessageViewSet

router = DefaultRouter()
router.register(r'menu', MenuItemViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'contact', ContactMessageViewSet)


urlpatterns = [
    path('', include(router.urls)),
]