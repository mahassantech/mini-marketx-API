from django.urls import path
from .views import ProductListApiView,ProductDetailApiView

urlpatterns = [
    path('', ProductListApiView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailApiView.as_view(), name='product-detail'),
]
