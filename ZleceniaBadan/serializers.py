from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ZleceniaBadan

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username')

class ZleceniaBadanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZleceniaBadan
        fields = ('imię', 'nazwisko', 'badanie', 'opis', 'wynik', 'termin')