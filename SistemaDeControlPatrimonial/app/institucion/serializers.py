from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from SistemaDeControlPatrimonial.app.institucion.models import Institucion, Sede, Local, Ambiente

class InstitucionSerializer(ModelSerializer):
	class Meta:
		model = Institucion
		fields = ('id', 'nombre','razon_social','direccion_fiscal','email','ruc')

	def create(self, request, validated_data):
		inst = Institucion.objects.create(**validated_data)
		inst.user = 'nefi'
		return inst

class SedePostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sede
