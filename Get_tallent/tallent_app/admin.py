from django.contrib import admin

from .models import Contractor, Employer, JobPost, Comment

# Register your models here.
class ContractorAdmin(admin.ModelAdmin):
    list_display = ["user","about"]
    
class EmployerAdmin(admin.ModelAdmin):
    list_display = ["user","about"]
    
class JobPostAdmin(admin.ModelAdmin):
    list_display = ["user","post"]
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user","comment"]




admin.site.register(Contractor, ContractorAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(JobPost, JobPostAdmin)
admin.site.register(Comment, CommentAdmin)