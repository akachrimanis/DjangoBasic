
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import ProductCategory

class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import ProductView

class ProductViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductView
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import ProductHistory

class ProductHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductHistory
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import DiscountInvoiceItem

class DiscountInvoiceItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiscountInvoiceItem
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import DiscountInvoice

class DiscountInvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiscountInvoice
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Discount

class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import ProductAttribute

class ProductAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductAttribute
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import ProductImage

class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import ProductStock

class ProductStockSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductStock
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Warehouse

class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import InventoryMovement

class InventoryMovementSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryMovement
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = "__all__"
        
        
from rest_framework import serializers
from .models import InvoiceItem

class InvoiceItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceItem
        fields = "__all__"
        
        
