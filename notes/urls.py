from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet,TraslateNote,StatiticsApi,PopularNotes
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register('notes' ,NoteViewSet,basename="notes")


urlpatterns = [
    path('',include(router.urls)),
    path('translate/<note_id>/',TraslateNote.as_view(),),
    path('stats/',StatiticsApi.as_view(),),
    path('popular_notes/',PopularNotes.as_view(),),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]


