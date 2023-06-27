from django.conf import settings
from rest_framework import serializers
from .models import libros


class librosSerializer(serializers.ModelSerializer):
    # Si su <field_name> se declara en su serializador con el parámetro required=False
    # Entonces este paso de validación no tendrá lugar si el campo no está incluido.
    created_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False, allow_null=True)
    updated_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False, allow_null=True)


    class Meta:
        model = libros
        fields = "__all__"
