from django.contrib import admin

from .models import *


class Ownerinline(admin.TabularInline):
    model = Owner.owned_apartments.through
    raw_id_fields = ("owner", "flat")


class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner")
    readonly_fields = ["created_at"]
    list_display = ("address", "price", "new_building", "construction_year", "town")
    list_editable = ["new_building"]
    list_filter = ("new_building", "rooms_number", "has_balcony")
    raw_id_fields = ["like"]
    inlines = [Ownerinline]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("name", "flat")


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("owned_apartments",)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
