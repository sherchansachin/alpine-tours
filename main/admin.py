from django.contrib import admin
from django.contrib.admin.decorators import action
from .models import Packages, Comment, RequestForm
# Register your models here.


admin.site.register(Packages)
admin.site.register(RequestForm)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'posted_on', 'active')
    list_filter = ('active', 'posted_on')
    search_fields = ('name', 'comment')
    actions = ['approve_comments']


    def approve_comments(self, request, queryset):
        queryset.update(active = True)