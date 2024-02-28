

import random
import sys
sys.path.append('/Users/tkax/dev/aimonetize/Backend/DjangoBasic/CRUDCreateCode')
import config
import config_fake_data

from faker import Faker
#from django.contrib.auth.models import User
from datetime import datetime
#import config
#import config_fake_data
import pandas as pd
fake = Faker()

# Generate a fake created_at timestamp within a specific range
def generate_fake_created_at(start_date, end_date):
    return fake.date_time_between(start_date=start_date, end_date=end_date)

# Example usage:
start_date = datetime(2020, 1, 1)  # Start date for the range
end_date = datetime.now()  # End date for the range (current date and time)
fake_created_at = generate_fake_created_at(start_date, end_date)

#from Product.models import Product  # Import your Customer model
# Define a function to generate fake Product data
def generate_fake_Products(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'name': fake.name(),
	'description': fake.description(),
	'price': fake.price(),
	'category': fake.category(),
	'created_at' : date_,
	'updated_at' : date_,
	'is_active': fake.is_active(),
	'available': fake.available(),
         }
        data.append(record)
    return data
Product_data = generate_fake_Products(num_records=config_fake_data.num_Product)

# Create a pandas DataFrame
df = pd.DataFrame(Product_data)

# Display the DataFrame
print(df)

#from ProductCategory.models import ProductCategory  # Import your Customer model
# Define a function to generate fake ProductCategory data
def generate_fake_ProductCategorys(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'name': fake.name(),
	'description': fake.description(),
	'parent': fake.parent(),
	'created_at' : date_,
	'updated_at' : date_,
	'slug': fake.slug(),
         }
        data.append(record)
    return data
ProductCategory_data = generate_fake_ProductCategorys(num_records=config_fake_data.num_ProductCategory)

# Create a pandas DataFrame
df = pd.DataFrame(ProductCategory_data)

# Display the DataFrame
print(df)

#from Order.models import Order  # Import your Customer model
# Define a function to generate fake Order data
def generate_fake_Orders(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user': fake.user(),
	'order_status': fake.order_status(),
	'total_amount': fake.total_amount(),
	'order_date': fake.order_date(),
	'shipping_address': fake.address(),
	'billing_address': fake.address(),
	'created_at' : date_,
	'updated_at' : date_,
	'payment': fake.payment(),
         }
        data.append(record)
    return data
Order_data = generate_fake_Orders(num_records=config_fake_data.num_Order)

# Create a pandas DataFrame
df = pd.DataFrame(Order_data)

# Display the DataFrame
print(df)

#from OrderItem.models import OrderItem  # Import your Customer model
# Define a function to generate fake OrderItem data
def generate_fake_OrderItems(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'order': fake.order(),
	'product': fake.product(),
	'quantity': fake.quantity(),
	'price_per_item': fake.price_per_item(),
	'discount_perc': fake.discount_perc(),
	'discount_type': fake.discount_type(),
	'total_price_after_discount': fake.total_price_after_discount(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
OrderItem_data = generate_fake_OrderItems(num_records=config_fake_data.num_OrderItem)

# Create a pandas DataFrame
df = pd.DataFrame(OrderItem_data)

# Display the DataFrame
print(df)

#from Address.models import Address  # Import your Customer model
# Define a function to generate fake Address data
def generate_fake_Addresss(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user': fake.user(),
	'address_line_1': fake.address(),
	'city': fake.city(),
	'state': fake.state(),
	'postal_code' : fake.zipcode(),
	'country': fake.country(),
	'is_shipping_addrss': fake.is_shipping_addrss(),
	'is_billing_address': fake.address(),
	'address_type': fake.address(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
Address_data = generate_fake_Addresss(num_records=config_fake_data.num_Address)

# Create a pandas DataFrame
df = pd.DataFrame(Address_data)

# Display the DataFrame
print(df)

#from Payment.models import Payment  # Import your Customer model
# Define a function to generate fake Payment data
def generate_fake_Payments(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'order': fake.order(),
	'amount': fake.amount(),
	'payment_method': fake.payment_method(),
	'payment_status': fake.payment_status(),
	'transaction_id': fake.transaction_id(),
	'payment_date': fake.payment_date(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
Payment_data = generate_fake_Payments(num_records=config_fake_data.num_Payment)

# Create a pandas DataFrame
df = pd.DataFrame(Payment_data)

# Display the DataFrame
print(df)

#from Review.models import Review  # Import your Customer model
# Define a function to generate fake Review data
def generate_fake_Reviews(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'product': fake.product(),
	'user': fake.user(),
	'rating': fake.rating(),
	'comment': fake.comment(),
	'review_date': fake.review_date(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
Review_data = generate_fake_Reviews(num_records=config_fake_data.num_Review)

# Create a pandas DataFrame
df = pd.DataFrame(Review_data)

# Display the DataFrame
print(df)

#from Cart.models import Cart  # Import your Customer model
# Define a function to generate fake Cart data
def generate_fake_Carts(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'user': fake.user(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
Cart_data = generate_fake_Carts(num_records=config_fake_data.num_Cart)

# Create a pandas DataFrame
df = pd.DataFrame(Cart_data)

# Display the DataFrame
print(df)

#from CartItem.models import CartItem  # Import your Customer model
# Define a function to generate fake CartItem data
def generate_fake_CartItems(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'cart': fake.cart(),
	'product': fake.product(),
	'quantity': fake.quantity(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
CartItem_data = generate_fake_CartItems(num_records=config_fake_data.num_CartItem)

# Create a pandas DataFrame
df = pd.DataFrame(CartItem_data)

# Display the DataFrame
print(df)

#from ProductView.models import ProductView  # Import your Customer model
# Define a function to generate fake ProductView data
def generate_fake_ProductViews(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'product': fake.product(),
	'user': fake.user(),
	'timestamp': fake.timestamp(),
	'action': fake.action(),
	'data_before': fake.data_before(),
	'data_after': fake.data_after(),
         }
        data.append(record)
    return data
ProductView_data = generate_fake_ProductViews(num_records=config_fake_data.num_ProductView)

# Create a pandas DataFrame
df = pd.DataFrame(ProductView_data)

# Display the DataFrame
print(df)

#from ProductHistory.models import ProductHistory  # Import your Customer model
# Define a function to generate fake ProductHistory data
def generate_fake_ProductHistorys(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'Product': fake.Product(),
	'User': fake.User(),
	'Timestamp': fake.Timestamp(),
	'Action': fake.Action(),
	'Data_before': fake.Data_before(),
	'Data_after': fake.Data_after(),
         }
        data.append(record)
    return data
ProductHistory_data = generate_fake_ProductHistorys(num_records=config_fake_data.num_ProductHistory)

# Create a pandas DataFrame
df = pd.DataFrame(ProductHistory_data)

# Display the DataFrame
print(df)

#from DiscountInvoiceItem.models import DiscountInvoiceItem  # Import your Customer model
# Define a function to generate fake DiscountInvoiceItem data
def generate_fake_DiscountInvoiceItems(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'name': fake.name(),
	'percentage': fake.percentage(),
	'start_date': fake.start_date(),
	'end_date': fake.end_date(),
	'products': fake.products(),
         }
        data.append(record)
    return data
DiscountInvoiceItem_data = generate_fake_DiscountInvoiceItems(num_records=config_fake_data.num_DiscountInvoiceItem)

# Create a pandas DataFrame
df = pd.DataFrame(DiscountInvoiceItem_data)

# Display the DataFrame
print(df)

#from DiscountInvoice.models import DiscountInvoice  # Import your Customer model
# Define a function to generate fake DiscountInvoice data
def generate_fake_DiscountInvoices(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'name': fake.name(),
	'percentage': fake.percentage(),
	'start_date': fake.start_date(),
	'end_date': fake.end_date(),
	'invoice': fake.invoice(),
         }
        data.append(record)
    return data
DiscountInvoice_data = generate_fake_DiscountInvoices(num_records=config_fake_data.num_DiscountInvoice)

# Create a pandas DataFrame
df = pd.DataFrame(DiscountInvoice_data)

# Display the DataFrame
print(df)

#from Discount.models import Discount  # Import your Customer model
# Define a function to generate fake Discount data
def generate_fake_Discounts(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'name': fake.name(),
	'percentage': fake.percentage(),
	'discount_type': fake.discount_type(),
	'created_at' : date_,
	'updated_at' : date_,
         }
        data.append(record)
    return data
Discount_data = generate_fake_Discounts(num_records=config_fake_data.num_Discount)

# Create a pandas DataFrame
df = pd.DataFrame(Discount_data)

# Display the DataFrame
print(df)

#from ProductAttribute.models import ProductAttribute  # Import your Customer model
# Define a function to generate fake ProductAttribute data
def generate_fake_ProductAttributes(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'product': fake.product(),
	'attribute': fake.attribute(),
	'value': fake.value(),
         }
        data.append(record)
    return data
ProductAttribute_data = generate_fake_ProductAttributes(num_records=config_fake_data.num_ProductAttribute)

# Create a pandas DataFrame
df = pd.DataFrame(ProductAttribute_data)

# Display the DataFrame
print(df)

#from ProductImage.models import ProductImage  # Import your Customer model
# Define a function to generate fake ProductImage data
def generate_fake_ProductImages(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'product': fake.product(),
	'image': fake.image(),
	'alt_text': fake.alt_text(),
	'end_date': fake.end_date(),
         }
        data.append(record)
    return data
ProductImage_data = generate_fake_ProductImages(num_records=config_fake_data.num_ProductImage)

# Create a pandas DataFrame
df = pd.DataFrame(ProductImage_data)

# Display the DataFrame
print(df)

#from ProductStock.models import ProductStock  # Import your Customer model
# Define a function to generate fake ProductStock data
def generate_fake_ProductStocks(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'product': fake.product(),
	'quantity': fake.quantity(),
         }
        data.append(record)
    return data
ProductStock_data = generate_fake_ProductStocks(num_records=config_fake_data.num_ProductStock)

# Create a pandas DataFrame
df = pd.DataFrame(ProductStock_data)

# Display the DataFrame
print(df)

#from Warehouse.models import Warehouse  # Import your Customer model
# Define a function to generate fake Warehouse data
def generate_fake_Warehouses(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'name': fake.name(),
	'location': fake.location(),
         }
        data.append(record)
    return data
Warehouse_data = generate_fake_Warehouses(num_records=config_fake_data.num_Warehouse)

# Create a pandas DataFrame
df = pd.DataFrame(Warehouse_data)

# Display the DataFrame
print(df)

#from InventoryMovement.models import InventoryMovement  # Import your Customer model
# Define a function to generate fake InventoryMovement data
def generate_fake_InventoryMovements(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'product_stock': fake.product_stock(),
	'movement_type': fake.movement_type(),
	'quantity': fake.quantity(),
	'movement_date': fake.movement_date(),
         }
        data.append(record)
    return data
InventoryMovement_data = generate_fake_InventoryMovements(num_records=config_fake_data.num_InventoryMovement)

# Create a pandas DataFrame
df = pd.DataFrame(InventoryMovement_data)

# Display the DataFrame
print(df)

#from Invoice.models import Invoice  # Import your Customer model
# Define a function to generate fake Invoice data
def generate_fake_Invoices(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'invoice_number': fake.invoice_number(),
	'date_created': fake.date_created(),
	'due_date': fake.due_date(),
	'customer': fake.customer(),
	'company_group': fake.company_group(),
	'company': fake.company(),
	'first_name' : fake.first_name(),
	'last_name' : fake.last_name(),
	'billing_address': fake.address(),
	'billing_address_city': fake.address(),
	'billing_address_state': fake.address(),
	'billing_address_postal_code': fake.address(),
	'billing_address_country': fake.address(),
	'shipping_address': fake.address(),
	'shipping_address_city': fake.address(),
	'shipping_address_state': fake.address(),
	'shipping_address_postal_code': fake.address(),
	'shipping_address_country': fake.address(),
	'contact_person': fake.contact_person(),
	'contact_email': fake.contact_email(),
	'contact_phone': fake.contact_phone(),
	'notes' : fake.text(),
	'tax_id': fake.tax_id(),
	'registration_number': fake.registration_number(),
	'payment_terms': fake.payment_terms(),
         }
        data.append(record)
    return data
Invoice_data = generate_fake_Invoices(num_records=config_fake_data.num_Invoice)

# Create a pandas DataFrame
df = pd.DataFrame(Invoice_data)

# Display the DataFrame
print(df)

#from InvoiceItem.models import InvoiceItem  # Import your Customer model
# Define a function to generate fake InvoiceItem data
def generate_fake_InvoiceItems(num_records):
    data = []
    date_ = fake.date()
    for _ in range(num_records):
        record = {
        # Generate fake data for specific fields
        	'product_code': fake.product_code(),
	'product_name': fake.product_name(),
	'product_quantity': fake.product_quantity(),
	'product_unit_price': fake.product_unit_price(),
	'vat_percentage': fake.vat_percentage(),
	'discount': fake.discount(),
	'payable': fake.payable(),
	'total_price': fake.total_price(),
	'total_vat': fake.total_vat(),
	'total_discount': fake.total_discount(),
	'total_payable': fake.total_payable(),
         }
        data.append(record)
    return data
InvoiceItem_data = generate_fake_InvoiceItems(num_records=config_fake_data.num_InvoiceItem)

# Create a pandas DataFrame
df = pd.DataFrame(InvoiceItem_data)

# Display the DataFrame
print(df)

