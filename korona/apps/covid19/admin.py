from django.contrib import admin
from .models import Health, Member, Holiday

admin.site.register(Health)
admin.site.register(Member)
admin.site.register(Holiday)

""" Django administration 変更 """
admin.site.site_header = 'Django 体調管理画面'

""" Site administration 変更 """
admin.site.index_title = 'モデルリスト'