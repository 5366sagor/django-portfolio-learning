from django.contrib import admin
from .models import Post
from .models import Skill
from .models import ContactMessage


admin.site.register(Post)
admin.site.register(Skill)
admin.site.register(ContactMessage)