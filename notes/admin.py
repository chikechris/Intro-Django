from django.contrib import admin 

from .models import Note 

class NoteAdmin(admin.ModelAdmin):
  readonly_fields = ('note_created_at', 'note_updated_at')

# Register your models here.
admin.site.register(Note, NoteAdmin)

