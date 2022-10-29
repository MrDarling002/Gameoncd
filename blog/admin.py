from django.contrib import admin
from .models import Game_category, Game_dev, Post, Category, Comment, Game

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, SlugAdmin)
admin.site.register(Category, SlugAdmin)
admin.site.register(Comment)
admin.site.register(Game, SlugAdmin)
admin.site.register(Game_category, SlugAdmin)
admin.site.register(Game_dev, SlugAdmin)




