from django.contrib import admin
from .models import *


# Register your models here.

# display post in list view for addmin

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", 'status', "created_on",)
    list_filter = ("status",)
    search_fields = ["title", "content"]


admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "post", "body", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ['approved_comments']

    def approved_comments(self,request,queryset):
        queryset.update(active=True)
