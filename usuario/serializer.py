from rest_framework import serializers
from rest_framework.exceptions import ValidationError as DrfValidationError

from empresa.models import Empresa, EmpresaMaster
from empresa.serializer import EmpresaSerializer, EmpresaMasterSerializer
from usuario.models import Usuario, Adm, Consultor
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.ModelSerializer):
    user_inf = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        data = validated_data
        validated_data = {'username': validated_data['username'],
                          'password': validated_data['password']}
        user_type = data['tipo']
        user = Usuario.objects.create(**data)
        try:
            self.create_user_by_type(user, user_type)
        except Exception as error:
            user.delete()
            raise error
        User.objects.create_user(**validated_data)
        return user

    def create_user_by_type(self, base_user, user_type):
        try:
            user_data = self.context['request'].data['user_inf']
        except Exception as erro:
            raise DrfValidationError({
                'error': 'Voce precisa passar as inforcoes do tipo de '
                         'usuario pela chave "user_inf"'})

        user_data['usuario'] = base_user.id
        serializer = USER_PROVIDERS[user_type][0](data=user_data)
        if serializer.is_valid():
            serializer.save()
        else:
            raise DrfValidationError(serializer.errors)

    def get_user_inf(self, base_user):
        serializer, model = USER_PROVIDERS[base_user.tipo]
        return serializer(model.objects.get(usuario=base_user.id)).data


class AdmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adm
        fields = "__all__"


class ConsultorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consultor
        fields = "__all__"


USER_PROVIDERS = {
    1: (AdmSerializer, Adm),
    2: (ConsultorSerializer, Consultor),
    3: (EmpresaSerializer, Empresa),
    4: (EmpresaMasterSerializer, EmpresaMaster),
}
