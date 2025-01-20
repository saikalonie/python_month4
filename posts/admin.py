from django.contrib import admin

from posts.models import Post, Category, Tag
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "rate", "created_at"]
    list_filter = ["category", "tags"]
    search_fields = ["title", "description", "tag_name"]

# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(Tag)