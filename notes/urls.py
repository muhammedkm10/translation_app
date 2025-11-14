from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet,TraslateNote

router = DefaultRouter()
router.register('notes' ,NoteViewSet,basename="notes")


urlpatterns = [
    path('',include(router.urls)),
    path('translate/<note_id>/',TraslateNote.as_view(),)
]
