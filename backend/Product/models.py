from django.db import models
from simple_history.models import HistoricalRecords



class Product(models.Model):
    name = models.CharField(max_length=255) 
    description = models.TextField() 
    price = models.DecimalField(max_digits=10,decimal_places=2) 
    stock_quantity = models.ForeignKey(ProductStock,on_delete=models.CASCADE,related_name='movements') 
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True) 
    available = models.BooleanField(default=True) 
    history = HistoricalRecords() 


class ProductCategory(models.Model):
    name = models.CharField(max_length=255) 
    description = models.TextField() 
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    slug = models.SlugField(max_length=255,unique=True) 
    history = HistoricalRecords() 


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    order_status = models.CharField(max_length=255) 
    total_amount = models.DecimalField(max_digits=10,decimal_places=2) 
    order_date = models.DateTimeField(auto_now_add=True) 
    shipping_address = models.ForeignKey(Address,related_name='shipping_address',on_delete=models.SET_NULL,null=True) 
    billing_address = models.ForeignKey(Address,related_name='billing_address',on_delete=models.SET_NULL,null=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,null=True) 
    history = HistoricalRecords() 


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE) 
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    quantity = models.IntegerField() 
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2) 
    discount_perc = models.DecimalField(max_digits=10, decimal_places=2) 
    discount_type = models.DecimalField(max_digits=10, decimal_places=2) 
    total_price_after_discount = models.DecimalField(max_digits=10, decimal_places=2) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    history = HistoricalRecords() 


class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    address_line_1 = models.CharField(max_length=255) 
    address_line_2 = models.CharField(max_length=255,blank=True) 
    city = models.CharField(max_length=255) 
    state = models.CharField(max_length=255) 
    postal_code = models.CharField(max_length=20) 
    country = models.CharField(max_length=255) 
    is_shipping_addrss = models.BooleanField(default=True) 
    is_billing_address = models.BooleanField(default=True) 
    address_type = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    history = HistoricalRecords() 


class Payment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE) 
    amount = models.DecimalField(max_digits=10,decimal_places=2) 
    payment_method = models.CharField(max_length=255) 
    payment_status = models.CharField(max_length=255) 
    transaction_id = models.CharField(max_length=255) 
    payment_date = models.DateTimeField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    history = HistoricalRecords() 


class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    rating = models.IntegerField() 
    comment = models.TextField() 
    review_date = models.DateTimeField(auto_now_add=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    history = HistoricalRecords() 


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    history = HistoricalRecords() 


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE) 
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    quantity = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    history = HistoricalRecords() 


class ProductView(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    timestamp = models.DateTimeField(default=timezone.now) 
    action = models.CharField(max_length=100) 
    data_before = models.JSONField() 
    data_after = models.JSONField() 
    history = HistoricalRecords() 


class ProductHistory(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    User = models.ForeignKey(User,on_delete=models.CASCADE) 
    Timestamp = models.DateTimeField(default=timezone.now) 
    Action = models.CharField(max_length=100) 
    Data_before = models.JSONField() 
    Data_after = models.JSONField() 
    history = HistoricalRecords() 


class DiscountInvoiceItem(models.Model):
    name = models.ForeignKey(Discount,on_delete=models.CASCADE) 
    percentage = models.DecimalField(max_digits=5,decimal_places=2,help_text="Percentage) 
    start_date = models.DateField() 
    end_date = models.DateField() 
    products = models.ManyToManyField(Product,blank=True,help_text="Products") 
    history = HistoricalRecords() 


class DiscountInvoice(models.Model):
    name = models.ForeignKey(Discount,on_delete=models.CASCADE) 
    percentage = models.DecimalField(max_digits=5,decimal_places=2,help_text="Percentage") 
    start_date = models.DateField() 
    end_date = models.DateField() 
    invoice = models.ManyToManyField(Invoice,blank=True,help_text="Invoices") 
    history = HistoricalRecords() 


class Discount(models.Model):
    name = models.CharField(max_length=255) 
    percentage = models.DecimalField(max_digits=5,decimal_places=2,help_text="Percentage") 
    type = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    history = HistoricalRecords() 


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product,related_name='attributes',on_delete=models.CASCADE) 
    attribute = models.CharField(max_length=255) 
    value = models.CharField(max_length=255) 
    history = HistoricalRecords() 


class ProductImage(models.Model):
    product = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='products/%Y/%m/%d') 
    alt_text = models.CharField(max_length=255,blank=True) 
    end_date = models.DateField() 


class ProductStock(models.Model):
    product = models.OneToOneField(Product,related_name='product stock',on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField() 
    history = HistoricalRecords() 


class Warehouse(models.Model):
    name = models.CharField(max_length=255) 
    location = models.CharField(max_length=255) 
    history = HistoricalRecords() 


class InventoryMovement(models.Model):
    product_stock = models.ForeignKey(ProductStock,on_delete=models.CASCADE,related_name='movements') 
    movement_type = models.CharField(max_length=50, choices=(('IN', 'Stock In'), ('OUT', 'Stock Out'))) 
    quantity = models.PositiveIntegerField() 
    movement_date = models.DateTimeField(auto_now_add=True) 
    history = HistoricalRecords() 


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True) 
    date_created = models.DateField(auto_now_add=True) 
    due_date = models.DateField(auto_now_add=True) 
    customer = models.ForeignKey(User, on_delete=models.CASCADE) 
    company_group = models.CharField(max_length=100,blank=True,null=True) 
    company = models.CharField(max_length=100) 
    firstname = models.CharField(max_length=100) 
    surname = models.CharField(max_length=100) 
    billing_address = models.CharField(max_length=255,blank=True,null=True) 
    billing_address_city = models.CharField(max_length=100,blank=True,null=True) 
    billing_address_state = models.CharField(max_length=100,blank=True,null=True) 
    billing_address_postal_code = models.CharField(max_length=20,blank=True,null=True) 
    billing_address_country = models.CharField(max_length=100,blank=True,null=True) 
    shipping_address = models.CharField(max_length=255,blank=True,null=True) 
    shipping_address_city = models.CharField(max_length=100,blank=True,null=True) 
    shipping_address_state = models.CharField(max_length=100,blank=True,null=True) 
    shipping_address_postal_code = models.CharField(max_length=20,blank=True,null=True) 
    shipping_address_country = models.CharField(max_length=100,blank=True,null=True) 
    contact_person = models.CharField(max_length=100,blank=True,null=True) 
    contact_email = models.EmailField(blank=True,null=True) 
    contact_phone = models.CharField(max_length=20,blank=True,null=True) 
    notes = models.TextField(blank=True,null=True) 
    tax_id = models.CharField(max_length=50,blank=True,null=True) 
    registration_number = models.CharField(max_length=50,blank=True,null=True) 
    payment_terms = models.CharField(max_length=100,blank=True,null=True) 
    history = HistoricalRecords() 


class InvoiceItem(models.Model):
    product_code = models.CharField(max_length=100,blank=True,null=True) 
    product_name = models.CharField(max_length=100,blank=True,null=True) 
    product_quantity = models.DecimalField(max_digits=15,decimal_places=2,blank=True,null=True) 
    product_unit_price = models.DecimalField(max_digits=15,decimal_places=2,blank=True,null=True) 
    vat_percentage = models.DecimalField(max_digits=15,decimal_places=2,blank=True,null=True) 
    discount = models.DecimalField(max_digits=15,decimal_places=2,blank=True,null=True) 
    payable = models.DecimalField(max_digits=15,decimal_places=2,blank=True,null=True) 
    total_price = models.DecimalField(max_digits=15,decimal_places=2,blank=True,null=True) 
    total_vat = models.DecimalField(max_digits=15,decimal_places=2,blank=True,null=True) 
    total_discount = models.DecimalField(max_digits=15,decimal_places=2,blank=True,null=True) 
    total_payable = models.DecimalField(max_digits=15,decimal_places=2,blank=True,null=True) 
    history = HistoricalRecords() 

