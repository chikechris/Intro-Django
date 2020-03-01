from django.db import models 
from uuid import uuid4

# Create your models here.

class Note(models.Model): 
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=200) 
  content = models.TextField(blank=True) 
  note_created_at = models.DateTimeField(auto_now_add=True)
  note_updated_at = models.DateTimeField(auto_now=True)
  url = models.URLField(blank=True)

