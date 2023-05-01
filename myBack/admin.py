from django.contrib import admin
from .models import *

admin.site.register(Publication)
admin.site.register(Type)
admin.site.register(Horaires_Roulements)
admin.site.register(Publi_HR)
admin.site.register(Publi_Type)

