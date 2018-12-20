from django.contrib import admin
from .models import TechType, TechProduct, TechReview

# Register your models here.
# Necessary if they are to appear in the admin
admin.site.register(TechType)
admin.site.register(TechProduct)
admin.site.register(TechReview)