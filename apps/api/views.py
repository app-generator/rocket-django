from apps.api.serializers import ProductSerializer
from apps.common.models import Product
from rest_framework import viewsets
from rest_framework import permissions


class ProductPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (ProductPermission, )
    lookup_field = 'id'