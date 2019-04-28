from django.contrib import admin

from accounts import models
# Register your models here.

class ApplicantAdmin(admin.ModelAdmin):
    list_display=['user','date_of_birth','contact_num1']

    search_fields=['user__username']

class ApplicationsAdmin(admin.ModelAdmin):
    list_display=['applicant','job','internship','applying_date_time']

    search_fields=['applying_date_time','applying_date','job__title']

class InterviewsAdmin(admin.ModelAdmin):
    list_display=['interview','hr_manager','applicant','interview_conducted_date_time']

    search_fields=['interview__job__title','hr_manager__name','interview_conducted_date_time']


class OffersAdmin(admin.ModelAdmin):
    list_display=['applicant','job','organization_name','offer_date_time']

    search_fields=['applicant','job','organization_name','offer_date_time']


admin.site.register(models.Profile)
admin.site.register(models.Reference)
admin.site.register(models.Hr_Manger)
admin.site.register(models.Applicant,ApplicantAdmin)
admin.site.register(models.Applications,ApplicationsAdmin)
admin.site.register(models.Interviews,InterviewsAdmin)
admin.site.register(models.offers,OffersAdmin)
admin.site.register(models.Job)
admin.site.register(models.Interview)
admin.site.register(models.Internship)
admin.site.register(models.InterviewQuestion)
admin.site.register(models.Experience)
admin.site.register(models.Databackup)
admin.site.register(models.Qualification)
admin.site.register(models.Resume)
