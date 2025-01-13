from django.contrib import admin
from .models import Player, Owner

# TODO: May not need Owner model
admin.site.register(Player)
admin.site.register(Owner)