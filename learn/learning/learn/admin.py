from django.contrib import admin
from .models import *

# Register your models here.
class chaiReviewInline(admin.TabularInline):
    model = chaiReviews
    # extra = 2 

class chaimenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'timedate')
    inlines = [chaiReviewInline]

class storeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal= ('chai_menu',)

class chaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'valid_until')

admin.site.register(chaimenu,chaimenuAdmin)
admin.site.register(chaiReviews)
admin.site.register(chaiCertificate,chaiCertificateAdmin)
admin.site.register(store,storeAdmin)