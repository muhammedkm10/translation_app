from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Note,Translation
from .serializers import NoteSerializer,TranslatorSerializer
from rest_framework import status
from rest_framework.response import Response
from .utility import translate_text_sync
from django.db.models import Count
from .caching_utility import increase_popularity
from django.core.cache import cache


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
            if not target_lan:
                return Response({'message':" target languages+ is required or it should be valid"},status=status.HTTP_400_BAD_REQUEST)
            already_exist  = Translation.objects.filter(note = note,translated_language = target_lan).exists()
            if already_exist:
                return Response({"message":"server error","details":"this note is already translated"},status = status.HTTP_400_BAD_REQUEST )
            increase_popularity(note_id = note_id)
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
            return Response({"message":"translated succesfully","result": {"transalted_text":response["result"],"original_text":note.original_text }},status = status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':"server error occured","details":str(e)},status=status.HTTP_400_BAD_REQUEST)




# statics api
class StatiticsApi(APIView):
    def get(self, request):
        try:
            # Total Notes
            total_notes = Note.objects.count()

            # Total Translations
            total_translations = Translation.objects.count()

            # Breakdown by original language
            notes_by_language_qs = (
                Note.objects.values("original_language")
                .annotate(count=Count("id"))
                .order_by()
            )

            notes_by_language = {
                item["original_language"]: item["count"]
                for item in notes_by_language_qs
            }

            # Breakdown of translation languages (OPTIONAL but useful)
            translations_by_language_qs = (
                Translation.objects.values("translated_language")
                .annotate(count=Count("id"))
                .order_by()
            )
            print(translations_by_language_qs)

            translations_by_language = {
                item["translated_language"]: item["count"]
                for item in translations_by_language_qs
            }

            return Response(
                {
                    "total_notes": total_notes,
                    "total_translations": total_translations,
                    "notes_by_language": notes_by_language,
                    "translations_by_language": translations_by_language,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response(
                {"message": "server error occured", "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )



class PopularNotes(APIView):
    def get(self, request):
        redis_client = cache.client.get_client()
        popular = redis_client.zrevrange("popular_notes", 0, 9, withscores=True)
        results = []
        for note_id, score in popular:
            note_id = int(note_id)

            # (Optional) Only fetch required note details
            try:
                note = Note.objects.get(id=note_id)
            except Note.DoesNotExist:
                continue

            results.append({
                "note_id": note.id,
                "title": note.title,
                "text": note.original_text,
                "translations_count": int(score)
            })

        return Response({"popular_notes": results})