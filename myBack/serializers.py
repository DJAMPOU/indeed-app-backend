from rest_framework import serializers
from .models import *

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class HRSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horaires_Roulements
        fields = '__all__'                     

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

class IdPubliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id']    

class IdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id']                 

class IdHRSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horaires_Roulements
        fields = ['id'] 

class PubliTypeSerializer(serializers.ModelSerializer):
    id_publi = IdPubliSerializer()
    id_type = IdTypeSerializer()
    class Meta:
        model = Publi_Type
        fields = ['id_type', 'id_publi'] 

class PubliHRSerializer(serializers.ModelSerializer):
    id_publi = IdPubliSerializer()
    id_hr = IdHRSerializer()
    class Meta:
        model = Publi_HR
        fields = ['id_publi', 'id_hr'] 
