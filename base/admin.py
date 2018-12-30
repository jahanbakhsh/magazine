from django.contrib import admin
from base.models import SubscriptionType, Settings, Message


class SubscriptionTypeAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'description', 'currency', 'active']
    list_display_links = ['id', 'title', 'description', 'currency', 'active']


class SettingsAdmin(admin.ModelAdmin):

    list_display_links = ['id', 'postalcode', 'email', 'telehphone', 'address']
    list_display = ['id', 'postalcode', 'email', 'telehphone', 'address']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'message', 'create_at']
    list_display_links = ['id', 'name', 'email', 'message', 'create_at']


admin.site.register(SubscriptionType, SubscriptionTypeAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(Message, MessageAdmin)
