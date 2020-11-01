from django.contrib import admin

from .models import Pet

#decorater
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    #to get rid of pets and vaccines being shown as object(1)
    list_display = ['name', 'species', 'breed', 'age', 'sex']
    
