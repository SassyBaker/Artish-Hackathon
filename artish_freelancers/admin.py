from django.contrib import admin
from .models import Freelancer, Skill, Tool, SocialLink


# Register your models here.
admin.site.register(Freelancer)
admin.site.register(Skill)
admin.site.register(Tool)
admin.site.register(SocialLink)
