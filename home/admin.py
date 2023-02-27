from django.contrib import admin

# Register your models here.
from .models import Item, Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Item, ItemAdmin)
admin.site.register(Comment)
# testing 