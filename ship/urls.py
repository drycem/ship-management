from django.urls import path
from . import views

app_name = 'ship'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/mdo_update', views.MdoUpdate.as_view(), name='mdo-update'),
    path('<int:pk>/fw_update', views.FwUpdate.as_view(), name='fw-update'),
]