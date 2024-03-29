
from django.contrib import admin
from django.urls import include, path
from tickets import views
from rest_framework.routers import DefaultRouter
from accounts.views import TroubleshootingTicketViewSet, ConversationViewSet, SystemResponseViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('reservations', views.views_reservation)
router.register('clients', views.viewsets_client)
router.register('films', views.views_film)

router.register(r'tickets', TroubleshootingTicketViewSet)
router.register(r'conversations', ConversationViewSet)
router.register(r'responses', SystemResponseViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    #1 
    path('django/jsonresponsenomodel/',views.no_rest_no_model),
    #2
    path('django/jsonresponsefrommodel',views.no_rest_from_model),
    #3 GET POST from rest framework
    path('rest/fbv/', views.FBV_list),
    #4 GET PUT DELETE PK from rest framework
    path('rest/fbv/<int:pk>/', views.FBV_pk),
    #5 GET POST FROM CLASS BASE VIEWS
    path('rest/CBV/', views.CBV_list.as_view()),
    #5 GET PUT DELETE FROM CLASS BASE VIEWS
    path('rest/CBV/<int:pk>/', views.CBV_pk.as_view()),
    #6 GET POST FROM CLASS BASE VIEWS MIXINS
    path('rest/mixins/', views.mixins_list.as_view()),
    #7 GET PUT DELETE FROM CLASS BASE VIEWS MIXINS
    path('rest/mixins/<int:pk>/', views.mixins_pk.as_view()),
    #8 GET POST generiv Class
    path('rest/generics/', views.generics_list.as_view()),
    #8 GET PUT DELETE generiv Class
    path('rest/generics/<int:pk>', views.generics_pk.as_view()),
    #9 viewsets 
    path('rest/viewsets/', include(router.urls)),

    path('api-auth', include('rest_framework.urls')),

    # API Token AUTH

    path('api-token-auth', obtain_auth_token),
]

