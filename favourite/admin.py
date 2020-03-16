from django.contrib import admin

from favourite.models import Favourite


class FavouriteAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'post', 'content'
    ]

    search_fields = [
        'user'
    ]

admin.site.register(Favourite, FavouriteAdmin)
