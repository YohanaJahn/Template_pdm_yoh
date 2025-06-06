from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import  CategoriaViewSet, UserViewSet, EditoraViewSet, AutorViewSet, LivroViewSet

router = DefaultRouter()

router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'editora', EditoraViewSet, basename='editora')
router.register(r'autor', AutorViewSet, basename='autor')
router.register(r'livro', LivroViewSet, basename='livros')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
