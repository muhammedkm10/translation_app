from django.db import models
from .languages import LANGUAGES

LANGUAGE_CHOICES = [(code, name) for code, name in LANGUAGES.items()]
# note model
class Note(models.Model):
    title = models.CharField(max_length=255)
    original_text = models.TextField()
    original_language = models.CharField(max_length=20,choices=LANGUAGE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# transaltion table 
class Translation(models.Model):
    note = models.ForeignKey(Note, related_name="translations", on_delete=models.CASCADE)
    translated_text = models.TextField()
    translated_language = models.CharField(max_length=20 ,choices = LANGUAGE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.note.title} → {self.translated_language}"
