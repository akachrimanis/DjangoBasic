from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

def home(request):
    return render(request, "home.html",{})


from .models import Product, ProductCategory, Order, OrderItem, Address, Payment, Review, Cart, CartItem, ProductView, ProductHistory, DiscountInvoiceItem, DiscountInvoice, Discount, ProductAttribute, ProductImage, ProductStock, Warehouse, InventoryMovement, Invoice, InvoiceItem
from .forms import ProductForm, ProductCategoryForm, OrderForm, OrderItemForm, AddressForm, PaymentForm, ReviewForm, CartForm, CartItemForm, ProductViewForm, ProductHistoryForm, DiscountInvoiceItemForm, DiscountInvoiceForm, DiscountForm, ProductAttributeForm, ProductImageForm, ProductStockForm, WarehouseForm, InventoryMovementForm, InvoiceForm, InvoiceItemForm
from .serializers import ProductSerializer, ProductCategorySerializer, OrderSerializer, OrderItemSerializer, AddressSerializer, PaymentSerializer, ReviewSerializer, CartSerializer, CartItemSerializer, ProductViewSerializer, ProductHistorySerializer, DiscountInvoiceItemSerializer, DiscountInvoiceSerializer, DiscountSerializer, ProductAttributeSerializer, ProductImageSerializer, ProductStockSerializer, WarehouseSerializer, InventoryMovementSerializer, InvoiceSerializer, InvoiceItemSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
     # Product Views  
class ProductListView(ListView):
    model = Product
    template_name = 'product-list.html'
    context_object_name = 'products'
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-details.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product-form.html'
    success_url = reverse_lazy('product-list')  # Redirect to the CRUD view after successful creation

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product-form.html'
    success_url = reverse_lazy('product-list')  # Redirect to the CRUD view after successful update

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product-confirm-delete.html'
    success_url = reverse_lazy('product-list')  # Redirect to the CRUD view after successful deletion
   
    

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    
     # ProductCategory Views  
class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'productcategory-list.html'
    context_object_name = 'productcategorys'
    
class ProductCategoryDetailView(DetailView):
    model = ProductCategory
    template_name = 'productcategory-details.html'
    context_object_name = 'productcategorys'

class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'productcategory-form.html'
    success_url = reverse_lazy('productcategory-list')  # Redirect to the CRUD view after successful creation

class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'productcategory-form.html'
    success_url = reverse_lazy('productcategory-list')  # Redirect to the CRUD view after successful update

class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'productcategory-confirm-delete.html'
    success_url = reverse_lazy('productcategory-list')  # Redirect to the CRUD view after successful deletion
   
    

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
     # Order Views  
class OrderListView(ListView):
    model = Order
    template_name = 'order-list.html'
    context_object_name = 'orders'
    
class OrderDetailView(DetailView):
    model = Order
    template_name = 'order-details.html'
    context_object_name = 'orders'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order-form.html'
    success_url = reverse_lazy('order-list')  # Redirect to the CRUD view after successful creation

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order-form.html'
    success_url = reverse_lazy('order-list')  # Redirect to the CRUD view after successful update

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order-confirm-delete.html'
    success_url = reverse_lazy('order-list')  # Redirect to the CRUD view after successful deletion
   
    

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
     # OrderItem Views  
class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'orderitem-list.html'
    context_object_name = 'orderitems'
    
class OrderItemDetailView(DetailView):
    model = OrderItem
    template_name = 'orderitem-details.html'
    context_object_name = 'orderitems'

class OrderItemCreateView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'orderitem-form.html'
    success_url = reverse_lazy('orderitem-list')  # Redirect to the CRUD view after successful creation

class OrderItemUpdateView(UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'orderitem-form.html'
    success_url = reverse_lazy('orderitem-list')  # Redirect to the CRUD view after successful update

class OrderItemDeleteView(DeleteView):
    model = OrderItem
    template_name = 'orderitem-confirm-delete.html'
    success_url = reverse_lazy('orderitem-list')  # Redirect to the CRUD view after successful deletion
   
    

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
     # Address Views  
class AddressListView(ListView):
    model = Address
    template_name = 'address-list.html'
    context_object_name = 'addresss'
    
class AddressDetailView(DetailView):
    model = Address
    template_name = 'address-details.html'
    context_object_name = 'addresss'

class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'address-form.html'
    success_url = reverse_lazy('address-list')  # Redirect to the CRUD view after successful creation

class AddressUpdateView(UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'address-form.html'
    success_url = reverse_lazy('address-list')  # Redirect to the CRUD view after successful update

class AddressDeleteView(DeleteView):
    model = Address
    template_name = 'address-confirm-delete.html'
    success_url = reverse_lazy('address-list')  # Redirect to the CRUD view after successful deletion
   
    

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
     # Payment Views  
class PaymentListView(ListView):
    model = Payment
    template_name = 'payment-list.html'
    context_object_name = 'payments'
    
class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payment-details.html'
    context_object_name = 'payments'

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment-form.html'
    success_url = reverse_lazy('payment-list')  # Redirect to the CRUD view after successful creation

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment-form.html'
    success_url = reverse_lazy('payment-list')  # Redirect to the CRUD view after successful update

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payment-confirm-delete.html'
    success_url = reverse_lazy('payment-list')  # Redirect to the CRUD view after successful deletion
   
    

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
     # Review Views  
class ReviewListView(ListView):
    model = Review
    template_name = 'review-list.html'
    context_object_name = 'reviews'
    
class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review-details.html'
    context_object_name = 'reviews'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review-form.html'
    success_url = reverse_lazy('review-list')  # Redirect to the CRUD view after successful creation

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review-form.html'
    success_url = reverse_lazy('review-list')  # Redirect to the CRUD view after successful update

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review-confirm-delete.html'
    success_url = reverse_lazy('review-list')  # Redirect to the CRUD view after successful deletion
   
    

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
     # Cart Views  
class CartListView(ListView):
    model = Cart
    template_name = 'cart-list.html'
    context_object_name = 'carts'
    
class CartDetailView(DetailView):
    model = Cart
    template_name = 'cart-details.html'
    context_object_name = 'carts'

class CartCreateView(CreateView):
    model = Cart
    form_class = CartForm
    template_name = 'cart-form.html'
    success_url = reverse_lazy('cart-list')  # Redirect to the CRUD view after successful creation

class CartUpdateView(UpdateView):
    model = Cart
    form_class = CartForm
    template_name = 'cart-form.html'
    success_url = reverse_lazy('cart-list')  # Redirect to the CRUD view after successful update

class CartDeleteView(DeleteView):
    model = Cart
    template_name = 'cart-confirm-delete.html'
    success_url = reverse_lazy('cart-list')  # Redirect to the CRUD view after successful deletion
   
    

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    
     # CartItem Views  
class CartItemListView(ListView):
    model = CartItem
    template_name = 'cartitem-list.html'
    context_object_name = 'cartitems'
    
class CartItemDetailView(DetailView):
    model = CartItem
    template_name = 'cartitem-details.html'
    context_object_name = 'cartitems'

class CartItemCreateView(CreateView):
    model = CartItem
    form_class = CartItemForm
    template_name = 'cartitem-form.html'
    success_url = reverse_lazy('cartitem-list')  # Redirect to the CRUD view after successful creation

class CartItemUpdateView(UpdateView):
    model = CartItem
    form_class = CartItemForm
    template_name = 'cartitem-form.html'
    success_url = reverse_lazy('cartitem-list')  # Redirect to the CRUD view after successful update

class CartItemDeleteView(DeleteView):
    model = CartItem
    template_name = 'cartitem-confirm-delete.html'
    success_url = reverse_lazy('cartitem-list')  # Redirect to the CRUD view after successful deletion
   
    

class ProductViewViewSet(viewsets.ModelViewSet):
    queryset = ProductView.objects.all()
    serializer_class = ProductViewSerializer
    
     # ProductView Views  
class ProductViewListView(ListView):
    model = ProductView
    template_name = 'productview-list.html'
    context_object_name = 'productviews'
    
class ProductViewDetailView(DetailView):
    model = ProductView
    template_name = 'productview-details.html'
    context_object_name = 'productviews'

class ProductViewCreateView(CreateView):
    model = ProductView
    form_class = ProductViewForm
    template_name = 'productview-form.html'
    success_url = reverse_lazy('productview-list')  # Redirect to the CRUD view after successful creation

class ProductViewUpdateView(UpdateView):
    model = ProductView
    form_class = ProductViewForm
    template_name = 'productview-form.html'
    success_url = reverse_lazy('productview-list')  # Redirect to the CRUD view after successful update

class ProductViewDeleteView(DeleteView):
    model = ProductView
    template_name = 'productview-confirm-delete.html'
    success_url = reverse_lazy('productview-list')  # Redirect to the CRUD view after successful deletion
   
    

class ProductHistoryViewSet(viewsets.ModelViewSet):
    queryset = ProductHistory.objects.all()
    serializer_class = ProductHistorySerializer
    
     # ProductHistory Views  
class ProductHistoryListView(ListView):
    model = ProductHistory
    template_name = 'producthistory-list.html'
    context_object_name = 'producthistorys'
    
class ProductHistoryDetailView(DetailView):
    model = ProductHistory
    template_name = 'producthistory-details.html'
    context_object_name = 'producthistorys'

class ProductHistoryCreateView(CreateView):
    model = ProductHistory
    form_class = ProductHistoryForm
    template_name = 'producthistory-form.html'
    success_url = reverse_lazy('producthistory-list')  # Redirect to the CRUD view after successful creation

class ProductHistoryUpdateView(UpdateView):
    model = ProductHistory
    form_class = ProductHistoryForm
    template_name = 'producthistory-form.html'
    success_url = reverse_lazy('producthistory-list')  # Redirect to the CRUD view after successful update

class ProductHistoryDeleteView(DeleteView):
    model = ProductHistory
    template_name = 'producthistory-confirm-delete.html'
    success_url = reverse_lazy('producthistory-list')  # Redirect to the CRUD view after successful deletion
   
    

class DiscountInvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = DiscountInvoiceItem.objects.all()
    serializer_class = DiscountInvoiceItemSerializer
    
     # DiscountInvoiceItem Views  
class DiscountInvoiceItemListView(ListView):
    model = DiscountInvoiceItem
    template_name = 'discountinvoiceitem-list.html'
    context_object_name = 'discountinvoiceitems'
    
class DiscountInvoiceItemDetailView(DetailView):
    model = DiscountInvoiceItem
    template_name = 'discountinvoiceitem-details.html'
    context_object_name = 'discountinvoiceitems'

class DiscountInvoiceItemCreateView(CreateView):
    model = DiscountInvoiceItem
    form_class = DiscountInvoiceItemForm
    template_name = 'discountinvoiceitem-form.html'
    success_url = reverse_lazy('discountinvoiceitem-list')  # Redirect to the CRUD view after successful creation

class DiscountInvoiceItemUpdateView(UpdateView):
    model = DiscountInvoiceItem
    form_class = DiscountInvoiceItemForm
    template_name = 'discountinvoiceitem-form.html'
    success_url = reverse_lazy('discountinvoiceitem-list')  # Redirect to the CRUD view after successful update

class DiscountInvoiceItemDeleteView(DeleteView):
    model = DiscountInvoiceItem
    template_name = 'discountinvoiceitem-confirm-delete.html'
    success_url = reverse_lazy('discountinvoiceitem-list')  # Redirect to the CRUD view after successful deletion
   
    

class DiscountInvoiceViewSet(viewsets.ModelViewSet):
    queryset = DiscountInvoice.objects.all()
    serializer_class = DiscountInvoiceSerializer
    
     # DiscountInvoice Views  
class DiscountInvoiceListView(ListView):
    model = DiscountInvoice
    template_name = 'discountinvoice-list.html'
    context_object_name = 'discountinvoices'
    
class DiscountInvoiceDetailView(DetailView):
    model = DiscountInvoice
    template_name = 'discountinvoice-details.html'
    context_object_name = 'discountinvoices'

class DiscountInvoiceCreateView(CreateView):
    model = DiscountInvoice
    form_class = DiscountInvoiceForm
    template_name = 'discountinvoice-form.html'
    success_url = reverse_lazy('discountinvoice-list')  # Redirect to the CRUD view after successful creation

class DiscountInvoiceUpdateView(UpdateView):
    model = DiscountInvoice
    form_class = DiscountInvoiceForm
    template_name = 'discountinvoice-form.html'
    success_url = reverse_lazy('discountinvoice-list')  # Redirect to the CRUD view after successful update

class DiscountInvoiceDeleteView(DeleteView):
    model = DiscountInvoice
    template_name = 'discountinvoice-confirm-delete.html'
    success_url = reverse_lazy('discountinvoice-list')  # Redirect to the CRUD view after successful deletion
   
    

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    
     # Discount Views  
class DiscountListView(ListView):
    model = Discount
    template_name = 'discount-list.html'
    context_object_name = 'discounts'
    
class DiscountDetailView(DetailView):
    model = Discount
    template_name = 'discount-details.html'
    context_object_name = 'discounts'

class DiscountCreateView(CreateView):
    model = Discount
    form_class = DiscountForm
    template_name = 'discount-form.html'
    success_url = reverse_lazy('discount-list')  # Redirect to the CRUD view after successful creation

class DiscountUpdateView(UpdateView):
    model = Discount
    form_class = DiscountForm
    template_name = 'discount-form.html'
    success_url = reverse_lazy('discount-list')  # Redirect to the CRUD view after successful update

class DiscountDeleteView(DeleteView):
    model = Discount
    template_name = 'discount-confirm-delete.html'
    success_url = reverse_lazy('discount-list')  # Redirect to the CRUD view after successful deletion
   
    

class ProductAttributeViewSet(viewsets.ModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
    
     # ProductAttribute Views  
class ProductAttributeListView(ListView):
    model = ProductAttribute
    template_name = 'productattribute-list.html'
    context_object_name = 'productattributes'
    
class ProductAttributeDetailView(DetailView):
    model = ProductAttribute
    template_name = 'productattribute-details.html'
    context_object_name = 'productattributes'

class ProductAttributeCreateView(CreateView):
    model = ProductAttribute
    form_class = ProductAttributeForm
    template_name = 'productattribute-form.html'
    success_url = reverse_lazy('productattribute-list')  # Redirect to the CRUD view after successful creation

class ProductAttributeUpdateView(UpdateView):
    model = ProductAttribute
    form_class = ProductAttributeForm
    template_name = 'productattribute-form.html'
    success_url = reverse_lazy('productattribute-list')  # Redirect to the CRUD view after successful update

class ProductAttributeDeleteView(DeleteView):
    model = ProductAttribute
    template_name = 'productattribute-confirm-delete.html'
    success_url = reverse_lazy('productattribute-list')  # Redirect to the CRUD view after successful deletion
   
    

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    
     # ProductImage Views  
class ProductImageListView(ListView):
    model = ProductImage
    template_name = 'productimage-list.html'
    context_object_name = 'productimages'
    
class ProductImageDetailView(DetailView):
    model = ProductImage
    template_name = 'productimage-details.html'
    context_object_name = 'productimages'

class ProductImageCreateView(CreateView):
    model = ProductImage
    form_class = ProductImageForm
    template_name = 'productimage-form.html'
    success_url = reverse_lazy('productimage-list')  # Redirect to the CRUD view after successful creation

class ProductImageUpdateView(UpdateView):
    model = ProductImage
    form_class = ProductImageForm
    template_name = 'productimage-form.html'
    success_url = reverse_lazy('productimage-list')  # Redirect to the CRUD view after successful update

class ProductImageDeleteView(DeleteView):
    model = ProductImage
    template_name = 'productimage-confirm-delete.html'
    success_url = reverse_lazy('productimage-list')  # Redirect to the CRUD view after successful deletion
   
    

class ProductStockViewSet(viewsets.ModelViewSet):
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer
    
     # ProductStock Views  
class ProductStockListView(ListView):
    model = ProductStock
    template_name = 'productstock-list.html'
    context_object_name = 'productstocks'
    
class ProductStockDetailView(DetailView):
    model = ProductStock
    template_name = 'productstock-details.html'
    context_object_name = 'productstocks'

class ProductStockCreateView(CreateView):
    model = ProductStock
    form_class = ProductStockForm
    template_name = 'productstock-form.html'
    success_url = reverse_lazy('productstock-list')  # Redirect to the CRUD view after successful creation

class ProductStockUpdateView(UpdateView):
    model = ProductStock
    form_class = ProductStockForm
    template_name = 'productstock-form.html'
    success_url = reverse_lazy('productstock-list')  # Redirect to the CRUD view after successful update

class ProductStockDeleteView(DeleteView):
    model = ProductStock
    template_name = 'productstock-confirm-delete.html'
    success_url = reverse_lazy('productstock-list')  # Redirect to the CRUD view after successful deletion
   
    

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    
     # Warehouse Views  
class WarehouseListView(ListView):
    model = Warehouse
    template_name = 'warehouse-list.html'
    context_object_name = 'warehouses'
    
class WarehouseDetailView(DetailView):
    model = Warehouse
    template_name = 'warehouse-details.html'
    context_object_name = 'warehouses'

class WarehouseCreateView(CreateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name = 'warehouse-form.html'
    success_url = reverse_lazy('warehouse-list')  # Redirect to the CRUD view after successful creation

class WarehouseUpdateView(UpdateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name = 'warehouse-form.html'
    success_url = reverse_lazy('warehouse-list')  # Redirect to the CRUD view after successful update

class WarehouseDeleteView(DeleteView):
    model = Warehouse
    template_name = 'warehouse-confirm-delete.html'
    success_url = reverse_lazy('warehouse-list')  # Redirect to the CRUD view after successful deletion
   
    

class InventoryMovementViewSet(viewsets.ModelViewSet):
    queryset = InventoryMovement.objects.all()
    serializer_class = InventoryMovementSerializer
    
     # InventoryMovement Views  
class InventoryMovementListView(ListView):
    model = InventoryMovement
    template_name = 'inventorymovement-list.html'
    context_object_name = 'inventorymovements'
    
class InventoryMovementDetailView(DetailView):
    model = InventoryMovement
    template_name = 'inventorymovement-details.html'
    context_object_name = 'inventorymovements'

class InventoryMovementCreateView(CreateView):
    model = InventoryMovement
    form_class = InventoryMovementForm
    template_name = 'inventorymovement-form.html'
    success_url = reverse_lazy('inventorymovement-list')  # Redirect to the CRUD view after successful creation

class InventoryMovementUpdateView(UpdateView):
    model = InventoryMovement
    form_class = InventoryMovementForm
    template_name = 'inventorymovement-form.html'
    success_url = reverse_lazy('inventorymovement-list')  # Redirect to the CRUD view after successful update

class InventoryMovementDeleteView(DeleteView):
    model = InventoryMovement
    template_name = 'inventorymovement-confirm-delete.html'
    success_url = reverse_lazy('inventorymovement-list')  # Redirect to the CRUD view after successful deletion
   
    

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
     # Invoice Views  
class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice-list.html'
    context_object_name = 'invoices'
    
class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoice-details.html'
    context_object_name = 'invoices'

class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice-form.html'
    success_url = reverse_lazy('invoice-list')  # Redirect to the CRUD view after successful creation

class InvoiceUpdateView(UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice-form.html'
    success_url = reverse_lazy('invoice-list')  # Redirect to the CRUD view after successful update

class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'invoice-confirm-delete.html'
    success_url = reverse_lazy('invoice-list')  # Redirect to the CRUD view after successful deletion
   
    

class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    
     # InvoiceItem Views  
class InvoiceItemListView(ListView):
    model = InvoiceItem
    template_name = 'invoiceitem-list.html'
    context_object_name = 'invoiceitems'
    
class InvoiceItemDetailView(DetailView):
    model = InvoiceItem
    template_name = 'invoiceitem-details.html'
    context_object_name = 'invoiceitems'

class InvoiceItemCreateView(CreateView):
    model = InvoiceItem
    form_class = InvoiceItemForm
    template_name = 'invoiceitem-form.html'
    success_url = reverse_lazy('invoiceitem-list')  # Redirect to the CRUD view after successful creation

class InvoiceItemUpdateView(UpdateView):
    model = InvoiceItem
    form_class = InvoiceItemForm
    template_name = 'invoiceitem-form.html'
    success_url = reverse_lazy('invoiceitem-list')  # Redirect to the CRUD view after successful update

class InvoiceItemDeleteView(DeleteView):
    model = InvoiceItem
    template_name = 'invoiceitem-confirm-delete.html'
    success_url = reverse_lazy('invoiceitem-list')  # Redirect to the CRUD view after successful deletion
   
    
