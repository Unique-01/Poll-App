from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Question)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question','choice_text']
