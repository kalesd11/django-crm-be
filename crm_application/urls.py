from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, SubscriptionViewSet, CardViewSet, AddressViewSet, BillViewSet,
    CustomerViewSet, LeadViewSet, ProjectViewSet, login, logout
)

router = DefaultRouter(trailing_slash=True)
router.register('users', UserViewSet, basename='users')
router.register('subscriptions', SubscriptionViewSet)
router.register('cards', CardViewSet)
router.register('addresses', AddressViewSet)
router.register('bills', BillViewSet)
router.register('customers', CustomerViewSet)
router.register('leads', LeadViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]