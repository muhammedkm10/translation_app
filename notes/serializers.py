from rest_framework import serializers 
from .models import Note,Translation


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        
        
class TranslatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = '__all__'