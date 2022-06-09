from django.urls import path
from api import views
from api.views import BibitaViewSet,TesseraViewSet,ColonnaViewSet


b_list = BibitaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
b_detail = BibitaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

t_list = BibitaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
t_detail = BibitaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


c_list = BibitaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
c_detail = BibitaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('bibite/', b_list, name='bibita-list'),
    path('bibite/<int:pk>/',b_detail, name='bibita-detail'),
    path('tessere/', t_list, name='tessera-list'),
    path('tessere/<int:pk>/',t_detail, name='tessera-detail'),
    path('colonne/', c_list, name='colonna-list'),
    path('colonne/<int:pk>/',c_detail, name='colonna-detail'),
    path('eroga/', views.eroga )

]