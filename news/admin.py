from django.contrib import admin
from news.models import News
from datetime import datetime

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title','image', 'date','source','created_at', 'updated_at', 'created_by', 'updated_by']
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    list_max_show_all =200
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
            obj.updated_at = datetime.now()
        else:
            obj.created_by = request.user
            obj.created_at = datetime.now()
            obj.updated_at = datetime.now()
        obj.save()

admin.site.register(News, NewsAdmin)