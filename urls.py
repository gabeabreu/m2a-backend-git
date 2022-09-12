from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView
from usuario.views import UserTokenObtainPairView


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
    path('', include('diagnostico.urls')),
    path('', include('empresa.urls')),
    path('', include('endereco.urls')),
    path('', include('questionario.urls')),
    path('', include('pergunta.urls')),
    path('', include('fundamento.urls')),
    path('', include('faturamento.urls')),
    path('', include('resposta.urls')),
    path('', include('segmento.urls')),
    path('', include('setor.urls')),
    path('', include('tipo_industria.urls')),
    path('', include('tipo_diagnostico.urls')),
    path('', include('valor_arrecadacao.urls')),
    path('', include('uf.urls')),
]

# Swagger
urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # noqa E501
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),  # noqa E501
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),  # noqa E501
]

urlpatterns += [
    path('login/', UserTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]
