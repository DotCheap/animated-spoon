from django.contrib import admin

# Register your models here.

from .models import SkillCat, Skills, User, Civility
admin.site.register(SkillCat)
admin.site.register(Skills)
admin.site.register(User)
admin.site.register(Civility)
