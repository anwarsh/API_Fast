
from django.contrib import admin
from django.urls import path
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #1 
    path('django/jsonresponsenomodel/',views.no_rest_no_model),
    #2
    path('django/jsonresponsefrommodel',views.no_rest_from_model),
    #3 GET POST from rest framework
    path('rest/fbv_list/', views.FBV_list),
    #4 GET PUT DELETE PK from rest framework
    path('rest/fbv_list/<int:pk>/', views.FBV_pk),
    #5 GET POST FROM CLASS BASE VIEWS
    path('rest/CBV_list/', views.CBV_list.as_view()),
    #5 GET PUT DELETE FROM CLASS BASE VIEWS
    path('rest/CBV_list/<int:pk>/', views.CBV_pk.as_view()),
    #6 GET POST FROM CLASS BASE VIEWS MIXINS
    path('rest/mixins_list/', views.mixins_list.as_view()),
    #7 GET PUT DELETE FROM CLASS BASE VIEWS MIXINS
    path('rest/mixins_list/<int:pk>/', views.mixins_pk.as_view())

]

