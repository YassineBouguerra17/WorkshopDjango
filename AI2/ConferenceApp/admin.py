from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_title = 'Conference Management 25/26'
admin.site.site_header = 'Conference Management 25/26'
admin.site.index_title = 'Conference Management 25/26'         

""""admin.site.register(CONFERENCE)"""
@admin.register(SUBMISSION)
class SUBMISSIONAdmin(admin.ModelAdmin):
    list_display = ('submission_id', 'title', 'status', 'payed', 'created_at', 'updated_at')
    search_fields = ('title', 'status', 'payed')
    list_filter = ('status', 'payed')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

class submissionInline(admin.StackedInline):
    model = SUBMISSION
    extra = 1
    readonly_fields =("submission_date",)

@admin.register(CONFERENCE)
class CONFERENCEpersonalization(admin.ModelAdmin):
    list_display = ('name', 'description', 'Theme', 'location', 'start_date', 'end_date', 'created_at', 'updated_at','duration')
    ordering = ('start_date', 'end_date')
    list_filter = ('name','Theme')
    search_fields = ('name', 'Theme')
    date_hierarchy = 'start_date'
    fieldsets = (
        ("information general",{
            "fields":('conference_id','name','Theme','description')
        }),
        ("logistic info",{
            "fields":('location','start_date','end_date')
        }),
    )
    readonly_fields = ('conference_id',)
    def duration(self, obj):
        if obj.start_date and obj.end_date:
            return (obj.end_date - obj.start_date).days
        return "RAS"
    duration.short_description = "Duration (days)"
    inlines = [submissionInline]