from django.contrib import admin

# Register your models here.
from .models import Cuisine, Food, Order

class CuisineAdmin(admin.ModelAdmin):
    list_display = ('category' , 'created_at')
    ordering = ('category',)


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name' , 'price', 'is_available')
    ordering = ('name',)
    list_aditable = ('is_available',)
    search_fields = ('name',)
    list_filter = ('is_available',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_details', 'is_ready', 'is_delivered')  # to display id, user, order_details, is_ready, is_delivered columns to the admin in admin page under Orders table
    list_editable = ('is_ready' , 'is_delivered')       # for check boxes
    ordering = ('-id', )

admin.site.register(Cuisine,CuisineAdmin)
admin.site.register(Food,FoodAdmin)
admin.site.register(Order,OrderAdmin)