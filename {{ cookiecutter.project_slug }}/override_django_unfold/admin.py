from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from allauth.account.admin import (
    EmailAddress,
    EmailAddressAdmin as BaseEmailAddressAdmin,
    EmailConfirmation,
    EmailConfirmationAdmin as BaseEmailConfirmationAdmin
)

from unfold.admin import ModelAdmin

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(EmailAddress)
admin.site.unregister(EmailConfirmation)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(EmailAddress)
class EmailAddressAdmin(BaseEmailAddressAdmin, ModelAdmin):
    pass

@admin.register(EmailConfirmation)
class EmailConfirmationAdmin(BaseEmailConfirmationAdmin, ModelAdmin):
    pass
