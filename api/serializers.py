from rest_framework import serializers
from .models import Bibita,Tessera,Colonna


class BibitaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bibita
        fields = ['id', 'codice', 'bevanda', 'prezzo']



class TesseraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tessera
        fields = ['id', 'codice', 'credito']


class ColonnaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colonna
        fields = ['numeroCol', 'bibita', 'numeroLatt']
