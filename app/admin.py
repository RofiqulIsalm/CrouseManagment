from django.contrib import admin
from .models import *
from app.models import CustormUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# class UserModel(UserAdmin):
#     list_display = ['username','user_type']
    
class what_you_learn_TabularInline(admin.TabularInline):
    model = What_you_learn
class Requirements_TabularInline(admin.TabularInline):
    model = Requirements
class Video_TabularInline(admin.TabularInline):
    model = Video
class couse_admin(admin.ModelAdmin):
    inlines = (what_you_learn_TabularInline, Requirements_TabularInline, Video_TabularInline)
    
admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course,couse_admin)
admin.site.register(Lavel)
admin.site.register(What_you_learn)
admin.site.register(Requirements)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(Language)
admin.site.register(UserCourse)
admin.site.register(Payment)
admin.site.register(CustormUser)