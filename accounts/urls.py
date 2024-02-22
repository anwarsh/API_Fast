from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TroubleshootingTicketViewSet, ConversationViewSet, SystemResponseViewSet

router = DefaultRouter()
router.register(r'tickets', TroubleshootingTicketViewSet)
router.register(r'conversations', ConversationViewSet)
router.register(r'responses', SystemResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
