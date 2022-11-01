from django.contrib import admin
from .models import Post, Tag, Rating, PostImage, Like




# соединяет несколько функций во единную (пост с фото и описанием )
class TabularInlineImages(admin.TabularInline):
    model = PostImage
    extra = 1
    fields = ['image']


class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [TabularInlineImages]

admin.site.register([ Tag, Rating, Like])
admin.site.register(Post, PostAdmin)






