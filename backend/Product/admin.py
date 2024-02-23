from django.contrib import admin
from .models import Product, ProductCategory, Order, OrderItem, Address, Payment, Review, Cart, CartItem, ProductView, ProductHistory, DiscountInvoiceItem, DiscountInvoice, Discount, ProductAttribute, ProductImage, ProductStock, Warehouse, InventoryMovement, Invoice, InvoiceItem
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ProductView)
admin.site.register(ProductHistory)
admin.site.register(DiscountInvoiceItem)
admin.site.register(DiscountInvoice)
admin.site.register(Discount)
admin.site.register(ProductAttribute)
admin.site.register(ProductImage)
admin.site.register(ProductStock)
admin.site.register(Warehouse)
admin.site.register(InventoryMovement)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)

