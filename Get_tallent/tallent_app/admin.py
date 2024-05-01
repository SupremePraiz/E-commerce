from django.contrib import admin

from .models import Contractor, Employer, JobPost, Comment

# Register your models here.



admin.site.register(Contractor)
admin.site.register(Employer)
admin.site.register(JobPost)
admin.site.register(Comment)