from django.contrib import admin
from .models import FavouriteBowls


class FavouriteBowlsAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_bowls')

    def display_bowls(self, obj):
        try:
            return ", ".join([bowl.name for bowl in obj.bowls.all()])
        except FavouriteBowls.DoesNotExist:
            return "No Favourite Bowls"

    display_bowls.short_description = 'Bowls'


admin.site.register(FavouriteBowls, FavouriteBowlsAdmin)
