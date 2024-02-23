from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .forms import *
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'productcategorys', views.ProductCategoryViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'orderitems', views.OrderItemViewSet)
router.register(r'addresss', views.AddressViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'carts', views.CartViewSet)
router.register(r'cartitems', views.CartItemViewSet)
router.register(r'productviews', views.ProductViewViewSet)
router.register(r'producthistorys', views.ProductHistoryViewSet)
router.register(r'discountinvoiceitems', views.DiscountInvoiceItemViewSet)
router.register(r'discountinvoices', views.DiscountInvoiceViewSet)
router.register(r'discounts', views.DiscountViewSet)
router.register(r'productattributes', views.ProductAttributeViewSet)
router.register(r'productimages', views.ProductImageViewSet)
router.register(r'productstocks', views.ProductStockViewSet)
router.register(r'warehouses', views.WarehouseViewSet)
router.register(r'inventorymovements', views.InventoryMovementViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'invoiceitems', views.InvoiceItemViewSet)
urlpatterns = [




    # products
    path('', views.ProductListView.as_view(), name='product-list'),
    path('create/', views.ProductCreateView.as_view(), name='product-create'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('<int:pk>/', views.ProductListView.as_view(), name='product-detail'),





    # productcategorys
    path('', views.ProductCategoryListView.as_view(), name='productcategory-list'),
    path('create/', views.ProductCategoryCreateView.as_view(), name='productcategory-create'),
    path('update/<int:pk>/', views.ProductCategoryUpdateView.as_view(), name='productcategory-update'),
    path('delete/<int:pk>/', views.ProductCategoryDeleteView.as_view(), name='productcategory-delete'),
    path('<int:pk>/', views.ProductCategoryListView.as_view(), name='productcategory-detail'),





    # orders
    path('', views.OrderListView.as_view(), name='order-list'),
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
    path('update/<int:pk>/', views.OrderUpdateView.as_view(), name='order-update'),
    path('delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order-delete'),
    path('<int:pk>/', views.OrderListView.as_view(), name='order-detail'),





    # orderitems
    path('', views.OrderItemListView.as_view(), name='orderitem-list'),
    path('create/', views.OrderItemCreateView.as_view(), name='orderitem-create'),
    path('update/<int:pk>/', views.OrderItemUpdateView.as_view(), name='orderitem-update'),
    path('delete/<int:pk>/', views.OrderItemDeleteView.as_view(), name='orderitem-delete'),
    path('<int:pk>/', views.OrderItemListView.as_view(), name='orderitem-detail'),





    # addresss
    path('', views.AddressListView.as_view(), name='address-list'),
    path('create/', views.AddressCreateView.as_view(), name='address-create'),
    path('update/<int:pk>/', views.AddressUpdateView.as_view(), name='address-update'),
    path('delete/<int:pk>/', views.AddressDeleteView.as_view(), name='address-delete'),
    path('<int:pk>/', views.AddressListView.as_view(), name='address-detail'),





    # payments
    path('', views.PaymentListView.as_view(), name='payment-list'),
    path('create/', views.PaymentCreateView.as_view(), name='payment-create'),
    path('update/<int:pk>/', views.PaymentUpdateView.as_view(), name='payment-update'),
    path('delete/<int:pk>/', views.PaymentDeleteView.as_view(), name='payment-delete'),
    path('<int:pk>/', views.PaymentListView.as_view(), name='payment-detail'),





    # reviews
    path('', views.ReviewListView.as_view(), name='review-list'),
    path('create/', views.ReviewCreateView.as_view(), name='review-create'),
    path('update/<int:pk>/', views.ReviewUpdateView.as_view(), name='review-update'),
    path('delete/<int:pk>/', views.ReviewDeleteView.as_view(), name='review-delete'),
    path('<int:pk>/', views.ReviewListView.as_view(), name='review-detail'),





    # carts
    path('', views.CartListView.as_view(), name='cart-list'),
    path('create/', views.CartCreateView.as_view(), name='cart-create'),
    path('update/<int:pk>/', views.CartUpdateView.as_view(), name='cart-update'),
    path('delete/<int:pk>/', views.CartDeleteView.as_view(), name='cart-delete'),
    path('<int:pk>/', views.CartListView.as_view(), name='cart-detail'),





    # cartitems
    path('', views.CartItemListView.as_view(), name='cartitem-list'),
    path('create/', views.CartItemCreateView.as_view(), name='cartitem-create'),
    path('update/<int:pk>/', views.CartItemUpdateView.as_view(), name='cartitem-update'),
    path('delete/<int:pk>/', views.CartItemDeleteView.as_view(), name='cartitem-delete'),
    path('<int:pk>/', views.CartItemListView.as_view(), name='cartitem-detail'),





    # productviews
    path('', views.ProductViewListView.as_view(), name='productview-list'),
    path('create/', views.ProductViewCreateView.as_view(), name='productview-create'),
    path('update/<int:pk>/', views.ProductViewUpdateView.as_view(), name='productview-update'),
    path('delete/<int:pk>/', views.ProductViewDeleteView.as_view(), name='productview-delete'),
    path('<int:pk>/', views.ProductViewListView.as_view(), name='productview-detail'),





    # producthistorys
    path('', views.ProductHistoryListView.as_view(), name='producthistory-list'),
    path('create/', views.ProductHistoryCreateView.as_view(), name='producthistory-create'),
    path('update/<int:pk>/', views.ProductHistoryUpdateView.as_view(), name='producthistory-update'),
    path('delete/<int:pk>/', views.ProductHistoryDeleteView.as_view(), name='producthistory-delete'),
    path('<int:pk>/', views.ProductHistoryListView.as_view(), name='producthistory-detail'),





    # discountinvoiceitems
    path('', views.DiscountInvoiceItemListView.as_view(), name='discountinvoiceitem-list'),
    path('create/', views.DiscountInvoiceItemCreateView.as_view(), name='discountinvoiceitem-create'),
    path('update/<int:pk>/', views.DiscountInvoiceItemUpdateView.as_view(), name='discountinvoiceitem-update'),
    path('delete/<int:pk>/', views.DiscountInvoiceItemDeleteView.as_view(), name='discountinvoiceitem-delete'),
    path('<int:pk>/', views.DiscountInvoiceItemListView.as_view(), name='discountinvoiceitem-detail'),





    # discountinvoices
    path('', views.DiscountInvoiceListView.as_view(), name='discountinvoice-list'),
    path('create/', views.DiscountInvoiceCreateView.as_view(), name='discountinvoice-create'),
    path('update/<int:pk>/', views.DiscountInvoiceUpdateView.as_view(), name='discountinvoice-update'),
    path('delete/<int:pk>/', views.DiscountInvoiceDeleteView.as_view(), name='discountinvoice-delete'),
    path('<int:pk>/', views.DiscountInvoiceListView.as_view(), name='discountinvoice-detail'),





    # discounts
    path('', views.DiscountListView.as_view(), name='discount-list'),
    path('create/', views.DiscountCreateView.as_view(), name='discount-create'),
    path('update/<int:pk>/', views.DiscountUpdateView.as_view(), name='discount-update'),
    path('delete/<int:pk>/', views.DiscountDeleteView.as_view(), name='discount-delete'),
    path('<int:pk>/', views.DiscountListView.as_view(), name='discount-detail'),





    # productattributes
    path('', views.ProductAttributeListView.as_view(), name='productattribute-list'),
    path('create/', views.ProductAttributeCreateView.as_view(), name='productattribute-create'),
    path('update/<int:pk>/', views.ProductAttributeUpdateView.as_view(), name='productattribute-update'),
    path('delete/<int:pk>/', views.ProductAttributeDeleteView.as_view(), name='productattribute-delete'),
    path('<int:pk>/', views.ProductAttributeListView.as_view(), name='productattribute-detail'),





    # productimages
    path('', views.ProductImageListView.as_view(), name='productimage-list'),
    path('create/', views.ProductImageCreateView.as_view(), name='productimage-create'),
    path('update/<int:pk>/', views.ProductImageUpdateView.as_view(), name='productimage-update'),
    path('delete/<int:pk>/', views.ProductImageDeleteView.as_view(), name='productimage-delete'),
    path('<int:pk>/', views.ProductImageListView.as_view(), name='productimage-detail'),





    # productstocks
    path('', views.ProductStockListView.as_view(), name='productstock-list'),
    path('create/', views.ProductStockCreateView.as_view(), name='productstock-create'),
    path('update/<int:pk>/', views.ProductStockUpdateView.as_view(), name='productstock-update'),
    path('delete/<int:pk>/', views.ProductStockDeleteView.as_view(), name='productstock-delete'),
    path('<int:pk>/', views.ProductStockListView.as_view(), name='productstock-detail'),





    # warehouses
    path('', views.WarehouseListView.as_view(), name='warehouse-list'),
    path('create/', views.WarehouseCreateView.as_view(), name='warehouse-create'),
    path('update/<int:pk>/', views.WarehouseUpdateView.as_view(), name='warehouse-update'),
    path('delete/<int:pk>/', views.WarehouseDeleteView.as_view(), name='warehouse-delete'),
    path('<int:pk>/', views.WarehouseListView.as_view(), name='warehouse-detail'),





    # inventorymovements
    path('', views.InventoryMovementListView.as_view(), name='inventorymovement-list'),
    path('create/', views.InventoryMovementCreateView.as_view(), name='inventorymovement-create'),
    path('update/<int:pk>/', views.InventoryMovementUpdateView.as_view(), name='inventorymovement-update'),
    path('delete/<int:pk>/', views.InventoryMovementDeleteView.as_view(), name='inventorymovement-delete'),
    path('<int:pk>/', views.InventoryMovementListView.as_view(), name='inventorymovement-detail'),





    # invoices
    path('', views.InvoiceListView.as_view(), name='invoice-list'),
    path('create/', views.InvoiceCreateView.as_view(), name='invoice-create'),
    path('update/<int:pk>/', views.InvoiceUpdateView.as_view(), name='invoice-update'),
    path('delete/<int:pk>/', views.InvoiceDeleteView.as_view(), name='invoice-delete'),
    path('<int:pk>/', views.InvoiceListView.as_view(), name='invoice-detail'),





    # invoiceitems
    path('', views.InvoiceItemListView.as_view(), name='invoiceitem-list'),
    path('create/', views.InvoiceItemCreateView.as_view(), name='invoiceitem-create'),
    path('update/<int:pk>/', views.InvoiceItemUpdateView.as_view(), name='invoiceitem-update'),
    path('delete/<int:pk>/', views.InvoiceItemDeleteView.as_view(), name='invoiceitem-delete'),
    path('<int:pk>/', views.InvoiceItemListView.as_view(), name='invoiceitem-detail'),


    path('api/1/', include(router.urls)),
    path('home/', views.home, name='home'),]
