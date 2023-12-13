from django.contrib import admin

# Register your models here.
from .models import TblCategoria,TblCurso

admin.site.register(TblCategoria)
admin.site.register(TblCurso)