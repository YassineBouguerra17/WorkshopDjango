from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_title = 'Conference Management 25/26'
admin.site.site_header = 'Conference Management 25/26'
admin.site.index_title = 'Conference Management 25/26'         

admin.site.register(CONFERENCE)
admin.site.register(SUBMISSION)

