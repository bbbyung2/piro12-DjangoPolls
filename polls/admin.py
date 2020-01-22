from django.contrib import admin

# Register your models here.
from .models import Question

admin.site.register(Question)  # admin page에서 app 보이게

