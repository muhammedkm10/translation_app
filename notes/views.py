from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Note,Translation
from .serializers import NoteSerializer,TranslatorSerializer
from rest_framework import status
from rest_framework.response import Response
from .utility import translate_text_sync
from .languages import LANGUAGES


# note api
class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    
    
  

# trasaltion api
class TraslateNote(APIView):
    def post(self,request,note_id):
        try:
            note = Note.objects.get(id= note_id)
            target_lan = request.data.get("target_lan")
            already_exist  = Translation.objects.get(note = note,translated_language = target_lan)
            if not target_lan:
                return Response({'message':" target languages is required or it should be valid"},status=status.HTTP_400_BAD_REQUEST)
            already_exist  = Translation.objects.filter(note = note,translated_language = target_lan).exists()
            if already_exist:
                return Response({"message":"server error","details":"this note is aleardy translated"},status = status.HTTP_400_BAD_REQUEST )
            response = translate_text_sync(note.original_text,note.original_language,target_lan)
            
            if not response["status"]:
                return Response({"message":"server error","details":str(response["result"])},status=status.HTTP_400_BAD_REQUEST)
            translation_data = {
                "note" : note.id,
                "translated_text" : response["result"],
                "translated_language" : target_lan
                
            }
            serializer = TranslatorSerializer(data = translation_data)
            if not  serializer.is_valid():
                return Response({'message':"server error occured","details":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            
            return Response({"message":"translated succesfully","result":response["result"]},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':"server error occured","details":str(e)},status=status.HTTP_400_BAD_REQUEST)
    
    
