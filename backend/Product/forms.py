from django import forms
from .serializers import ProductSerializer
from .models import Product



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'is_active', 'available']
        # Add any other fields that you have in your Customer model


from .serializers import ProductCategorySerializer
from .models import ProductCategory



class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description', 'parent', 'slug']
        # Add any other fields that you have in your Customer model


from .serializers import OrderSerializer
from .models import Order



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'order_status', 'total_amount', 'shipping_address', 'billing_address', 'payment']
        # Add any other fields that you have in your Customer model


from .serializers import OrderItemSerializer
from .models import OrderItem



class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'price_per_item', 'discount_perc', 'discount_type', 'total_price_after_discount']
        # Add any other fields that you have in your Customer model


from .serializers import AddressSerializer
from .models import Address



class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['user', 'address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country', 'is_shipping_addrss', 'is_billing_address', 'address_type']
        # Add any other fields that you have in your Customer model


from .serializers import PaymentSerializer
from .models import Payment



class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['order', 'amount', 'payment_method', 'payment_status', 'transaction_id', 'payment_date']
        # Add any other fields that you have in your Customer model


from .serializers import ReviewSerializer
from .models import Review



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'user', 'rating', 'comment', ]
        # Add any other fields that you have in your Customer model


from .serializers import CartSerializer
from .models import Cart



class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user']
        # Add any other fields that you have in your Customer model


from .serializers import CartItemSerializer
from .models import CartItem



class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity']
        # Add any other fields that you have in your Customer model


from .serializers import ProductViewSerializer
from .models import ProductView



class ProductViewForm(forms.ModelForm):
    class Meta:
        model = ProductView
        fields = ['product', 'user', 'timestamp', 'action', 'data_before', 'data_after']
        # Add any other fields that you have in your Customer model


from .serializers import ProductHistorySerializer
from .models import ProductHistory



class ProductHistoryForm(forms.ModelForm):
    class Meta:
        model = ProductHistory
        fields = ['Product', 'User', 'Timestamp', 'Action', 'Data_before', 'Data_after']
        # Add any other fields that you have in your Customer model


from .serializers import DiscountInvoiceItemSerializer
from .models import DiscountInvoiceItem



class DiscountInvoiceItemForm(forms.ModelForm):
    class Meta:
        model = DiscountInvoiceItem
        fields = ['name', 'percentage', 'start_date', 'end_date', 'products']
        # Add any other fields that you have in your Customer model


from .serializers import DiscountInvoiceSerializer
from .models import DiscountInvoice



class DiscountInvoiceForm(forms.ModelForm):
    class Meta:
        model = DiscountInvoice
        fields = ['name', 'percentage', 'start_date', 'end_date', 'invoice']
        # Add any other fields that you have in your Customer model


from .serializers import DiscountSerializer
from .models import Discount



class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['name', 'percentage', 'discount_type']
        # Add any other fields that you have in your Customer model


from .serializers import ProductAttributeSerializer
from .models import ProductAttribute



class ProductAttributeForm(forms.ModelForm):
    class Meta:
        model = ProductAttribute
        fields = ['product', 'attribute', 'value']
        # Add any other fields that you have in your Customer model


from .serializers import ProductImageSerializer
from .models import ProductImage



class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['product', 'image', 'alt_text', 'end_date']
        # Add any other fields that you have in your Customer model


from .serializers import ProductStockSerializer
from .models import ProductStock



class ProductStockForm(forms.ModelForm):
    class Meta:
        model = ProductStock
        fields = ['product', 'quantity']
        # Add any other fields that you have in your Customer model


from .serializers import WarehouseSerializer
from .models import Warehouse



class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name', 'location']
        # Add any other fields that you have in your Customer model


from .serializers import InventoryMovementSerializer
from .models import InventoryMovement



class InventoryMovementForm(forms.ModelForm):
    class Meta:
        model = InventoryMovement
        fields = ['product_stock', 'movement_type', 'quantity']
        # Add any other fields that you have in your Customer model


from .serializers import InvoiceSerializer
from .models import Invoice



class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'due_date', 'customer', 'company_group', 'company', 'firstname', 'surname', 'billing_address', 'billing_address_city', 'billing_address_state', 'billing_address_postal_code', 'billing_address_country', 'shipping_address', 'shipping_address_city', 'shipping_address_state', 'shipping_address_postal_code', 'shipping_address_country', 'contact_person', 'contact_email', 'contact_phone', 'notes', 'tax_id', 'registration_number', 'payment_terms']
        # Add any other fields that you have in your Customer model


from .serializers import InvoiceItemSerializer
from .models import InvoiceItem



class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['product_code', 'product_name', 'product_quantity', 'product_unit_price', 'vat_percentage', 'discount', 'payable', 'total_price', 'total_vat', 'total_discount', 'total_payable']
        # Add any other fields that you have in your Customer model


