from django.contrib import admin
from .models import *

# Register your models here.

class RoomMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_name', 'uid')

    list_filter = ('room_name','name')

    search_fields = ('name', 'room_name')


admin.site.register(RoomMember,RoomMemberAdmin)


