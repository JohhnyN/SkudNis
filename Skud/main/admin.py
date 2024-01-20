from django.contrib import admin
from . import models


class OfficeAdmin(admin.ModelAdmin):
    list_display = ("office", "time_created", "time_updated", "active", "busy")
    search_fields = ("office",)
    list_editable = ("active",)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "photo", "job_title", "phone", "time_created", "time_updated", "active")
    search_fields = ("name",)
    list_editable = ("active",)
    prepopulated_fields = {"slug": ("name",)}


class HistoryAdmin(admin.ModelAdmin):
    list_display = ("office", "teacher", "start_time", "end_time", "returned")
    search_fields = ("office",)
    list_editable = ("returned",)


admin.site.register(models.Office, OfficeAdmin)
admin.site.register(models.Teacher, TeacherAdmin)
admin.site.register(models.CardHistory, HistoryAdmin)
