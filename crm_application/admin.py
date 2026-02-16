from django.contrib import admin
from .models import Subscription, Address, Bill, Customer, Project, Lead, Card

# Register your models here.
admin.site.register(Subscription)
admin.site.register(Address)
admin.site.register(Bill)
admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Lead)
admin.site.register(Card)


# @admin.register(Card)
# class ApplicationAdmin(admin.ModelAdmin):
#     pass