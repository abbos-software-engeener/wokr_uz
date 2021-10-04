from django.contrib import admin
from .models import *


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Shipper)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = [
#         "id",
#         'comment',
#     ]
#
#     class Meta:
#
#         model = Comment
#
#
# admin.site.register(Comment, CommentAdmin )

admin.site.register(Carrier)

admin.site.register(ContactUser)

admin.site.register(AboutUs)

admin.site.register(OurService)