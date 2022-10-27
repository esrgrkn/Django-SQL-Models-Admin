from django.contrib import admin
from .models import ProductType,Supplier,Product,ContactForm

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","stockStatus","selected_categories",)
    list_display_links = ("name","price")
    list_filter = ("name","price",)
    list_editable = ("stockStatus",)
    search_fields = ("name","description")

    def selected_categories(self, obj):
        html = ""

        for category in obj.categories.all():
            html += category.name + " "

        return html    

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(ProductType)
admin.site.register(ContactForm)

