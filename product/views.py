import logging
from rest_framework import viewsets
from .models import Category,Product
from .serializer import CategorySerializer,ProductSerializer

logger = logging.getLogger(__name__)

class CategoryView(viewsets.ModelViewSet):
    logger.info('Информационное сообщение')
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(viewsets.ModelViewSet):
    logger.debug('')
    queryset = Product.objects.all()
    serializer_class = ProductSerializer