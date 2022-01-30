from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ("name", "url","position","posted",)
    list_display_links = ("name",)
    list_editable = ("posted","position",)

    icon_name = 'dehaze'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "description")
    list_display_links = ("name",)

    icon_name = 'folder_open'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "date", "posted", "get_image",)
    list_display_links = ("title",)
    list_editable = ("posted",)
    readonly_fields = ("get_image", "id",)
    search_fields = ("title",)
    save_on_top = True
    save_as = True

    icon_name = 'description'

    def get_image(self, obj):
        return mark_safe(f'<img src="/media/{obj.img}" width="50px" >')

    get_image.short_description = 'Картинка поста'
