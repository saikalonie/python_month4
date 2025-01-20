from django.contrib import admin

from posts.models import Post, Category, Tag
<<<<<<< HEAD
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "rate", "created_at"]
    list_filter = ["category", "tags"]
    search_fields = ["title", "description", "tag_name"]
=======

admin.site.register(Post)
>>>>>>> d0a8e2e1d6f04fff339d55bbc5e72f56566b62bb
admin.site.register(Category)
admin.site.register(Tag)