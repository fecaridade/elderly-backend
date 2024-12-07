from django.urls import path,include
from rest_framework.routers import DefaultRouter

from api.views import AtividadeViewSet

app_name = "api"


route = DefaultRouter()
route.register("atividades",AtividadeViewSet,basename="atividades")



urlpatterns = [
    path("",include(route.urls))
]
