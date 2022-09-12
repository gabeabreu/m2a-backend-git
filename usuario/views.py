from rest_framework import viewsets

from usuario.serializer import UsuarioSerializer, AdmSerializer, \
    ConsultorSerializer
from usuario.models import Usuario, Adm, Consultor
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter()
    serializer_class = UsuarioSerializer
    model_class = Usuario
    user_class = True
    filter_fields = '__all__'


class AdmViewSet(viewsets.ModelViewSet):
    queryset = Adm.objects.filter()
    serializer_class = AdmSerializer
    model_class = Adm
    user_class = True
    filter_fields = '__all__'


class ConsultorViewSet(viewsets.ModelViewSet):
    queryset = Consultor.objects.filter()
    serializer_class = ConsultorSerializer
    model_class = Consultor
    user_class = True
    filter_fields = '__all__'


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        user = Usuario.objects.get(username=self.user.username)
        data['user'] = UsuarioSerializer(user).data
        return data


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
