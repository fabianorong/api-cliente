from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

    def validate(self, data):
        if not cpf_valido(data["cpf"]):
            raise serializers.ValidationError({"cpf": "numero de cpf invalido"})
        if not nome_valido(data["nome"]):
            raise serializers.ValidationError(
                {"nome": "nao inclua numeros neste campo"}
            )
        if not rg_valido(data["rg"]):
            raise serializers.ValidationError({"rg": "o rg deve ter 9 digitos"})

        if not celular_valido(data["celular"]):
            raise serializers.ValidationError(
                {
                    "celular": "o numero de celular deve seguir este modelo: 11 12345-6789"
                }
            )
        return data
