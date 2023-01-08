from django.contrib import admin
from django.http import HttpResponse
import csv
from admin_interface_app import models

class ExportCsvMixin():
    def export(self, request, queryset):
        # get model info
        meta = self.model._meta
        # get field name
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)

        # create a writer
        writer = csv.writer(response)

        # write fields name
        writer.writerow(field_names)

        # write content
        for object in queryset:
            row = writer.writerow([getattr(object, field) for field in field_names])
        return response
    export.short_description = 'Export Selected'

class MovieAdmin(admin.ModelAdmin, ExportCsvMixin):
    fields = ('year', 'title', 'length')
    search_fields = ('year', 'title')
    list_filter = ['year', 'length']
    list_display = ['title', 'year', 'length', 'id']
    # for editable you need 'list_display'
    list_editable = ['year', 'length']

    actions = ["export"]

# Register your models here.
admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Customer)
