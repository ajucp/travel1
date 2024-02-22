from django.contrib import admin

# Register your models here.
from . models import Place
admin.site.register(Place)
from . models import reviewer
admin.site.register(reviewer)
from . models import reviews
admin.site.register(reviews)