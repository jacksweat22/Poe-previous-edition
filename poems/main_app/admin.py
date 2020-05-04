from django.contrib import admin
from .models import Poem, Comment
# Register your models here.
admin.site.register(Poem)
admin.site.register(Comment)