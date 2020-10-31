from django.contrib import admin

from .models import User, Video, Vote


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ['votes']

#Register your models here.
admin.site.register(User)
admin.site.register(Video, VideoAdmin)
admin.site.register(Vote)