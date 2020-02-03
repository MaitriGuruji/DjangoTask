from django.contrib import admin

# Register your models here.
from .models import UsrPost,User,Comment
admin.site.register(UsrPost)
admin.site.register(User)
admin.site.register(Comment)
