from django.contrib import admin
from .models import Project,ProjectFeature,ProjectImage,ProjectVideo,Skill,Title,Bio,Contact,ContactIcon
# Register your models here.

admin.site.register([Project,ProjectFeature,ProjectImage,ProjectVideo,Skill,Title,Bio,Contact,ContactIcon])