from django.contrib import admin

# Register your models here.
from .models import Area, Organization, Building


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created', 'updated')
    list_display_links = ('pk', 'name')
    list_filter = ('created', 'updated')


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'formed', 'area', 'created', 'updated')
    list_display_links = ('pk', 'name')
    list_filter = ('area', 'created', 'updated')


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'organization', 'area', 'land_area', 'floor', 'parking_lot', 'playground', 'elevator',
                    'created', 'updated')
    list_display_links = ('pk', 'name')
    list_filter = ('name', 'organization', 'area', 'created', 'updated')
