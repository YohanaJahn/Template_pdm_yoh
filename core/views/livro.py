from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers import LivroSerializers

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers