from django.contrib import admin

from .models import *

admin.site.register(Book)


admin.site.register(Journal)

# class MyModelAdmin(admin.ModelAdmin):
#
#     def has_change_permission(self, request, obj=None):
#         if obj is not None and obj.created_by != request.user:
#             return False
#         return True
#
#     def has_delete_permission(self, request, obj=None):
#         if obj is not None and obj.created_by != request.user:
#             return False
#         return True