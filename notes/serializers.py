from rest_framework import serializers 
from .models import Note,Translation



        
class TranslatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = '__all__'
        
class NoteSerializer(serializers.ModelSerializer):
    translations = TranslatorSerializer(many = True,read_only = True)
    class Meta:
        model = Note
        fields = ['id','title','original_text','original_language','created_at','translations']
        