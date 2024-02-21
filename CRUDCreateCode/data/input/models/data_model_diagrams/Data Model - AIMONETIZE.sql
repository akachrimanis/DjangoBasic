CREATE TABLE "Employee" (
  "id" integer PRIMARY KEY,
  "first_name" Char,
  "surname" Char,
  "age" PositiveInteger,
  "email" Email,
  "phone" Char,
  "address" Char,
  "department" Char,
  "role" Char,
  "employer" ForeignKey,
  "manager" ForeignKey,
  "organization" ForeignKey
);

CREATE TABLE "Employer" (
  "id" integer PRIMARY KEY,
  "company_name" Char,
  "password" Char,
  "email" Email,
  "name" Char,
  "organization" ForeignKey,
  "history" HistoricalRecords
);

CREATE TABLE "Individual" (
  "id" integer PRIMARY KEY,
  "history" HistoricalRecords,
  "employee" ForeignKey,
  "user" OneToOne
);

CREATE TABLE "Manager" (
  "id" integer PRIMARY KEY,
  "first_name" Char,
  "surname" Char,
  "age" PositiveInteger,
  "email" Email,
  "phone" Char,
  "address" Char,
  "department" Char,
  "role" Char,
  "employer" ForeignKey,
  "organization" ForeignKey
);

CREATE TABLE "Organization" (
  "id" integer PRIMARY KEY,
  "name" Char,
  "address" Char,
  "history" HistoricalRecords
);

CREATE TABLE "CustomerB2B" (
  "id" integer PRIMARY KEY,
  "name" Char,
  "history" HistoricalRecords,
  "updated_at" DateTime,
  "created_at" DateTime,
  "notes" Text,
  "company_group" Char,
  "bank_account_number" Char,
  "bank_name" Char,
  "payment_terms" Char,
  "registration_number" Char,
  "tax_id" Char,
  "annual_revenue" Decimal,
  "company_size" PositiveInteger,
  "swift_code" Char,
  "contact_phone" Char,
  "contact_email" Email,
  "contact_person" Char,
  "country" Char,
  "postal_code" Char,
  "state" Char,
  "city" Char,
  "address_line_2" Char,
  "address_line_1" Char,
  "website" URL,
  "phone" Char,
  "email" Email,
  "industry" Char
);

CREATE TABLE "CustomerB2BAggregate_country" (
  "id" integer PRIMARY KEY,
  "country" Char,
  "total_customers" Char,
  "total_industries" Integer,
  "total_company_size" PositiveInteger,
  "total_annual_revenue" Decimal
);

CREATE TABLE "CustomerB2BGoup" (
  "id" integer PRIMARY KEY,
  "registration_number" Char,
  "updated_at" DateTime,
  "history" HistoricalRecords,
  "created_at" DateTime,
  "notes" Text,
  "company_group" Char,
  "swift_code" Char,
  "bank_account_number" Char,
  "bank_name" Char,
  "payment_terms" Char,
  "tax_id" Char,
  "city" Char,
  "company_size" PositiveInteger,
  "name" Char,
  "email" Email,
  "phone" Char,
  "annual_revenue" Decimal,
  "address_line_1" Char,
  "address_line_2" Char,
  "website" URL,
  "postal_code" Char,
  "country" Char,
  "contact_person" Char,
  "contact_email" Email,
  "contact_phone" Char,
  "industry" Char,
  "state" Char
);

CREATE TABLE "CustomerUserProfileB2B" (
  "id" integer PRIMARY KEY,
  "description" Char,
  "company" ForeignKey,
  "username" Char,
  "firstname" Char,
  "surname" Char,
  "email" Email,
  "phone" Char,
  "history" HistoricalRecords
);

CREATE TABLE "CustomerB2C" (
  "id" integer PRIMARY KEY,
  "firstname" Char,
  "history" HistoricalRecords,
  "updated_at" DateTime,
  "created_at" DateTime,
  "notes" Text,
  "postal_code" Char,
  "state" Char,
  "city" Char,
  "country" Char,
  "address_line_1" Char,
  "website" URL,
  "phone" Char,
  "email" Email,
  "date_of_birth" Date,
  "surname" Char,
  "address_line_2" Char
);

CREATE TABLE "CustomerUserProfileB2C" (
  "id" integer PRIMARY KEY,
  "last_login" Char,
  "username" Char,
  "firstname" Char,
  "surname" Char,
  "email" Email,
  "phone" Char,
  "history" HistoricalRecords
);

CREATE TABLE "Customer" (
  "id" integer PRIMARY KEY,
  "date" DateTime,
  "price" Integer,
  "created_at" DateTime,
  "updated_at" DateTime
);

CREATE TABLE "Address" (
  "id" integer PRIMARY KEY,
  "state" Char,
  "history" HistoricalRecords,
  "updated_at" DateTime,
  "created_at" DateTime,
  "address_type" Char,
  "is_billing_address" Boolean,
  "country" Char,
  "is_shipping_addrss" Boolean,
  "user" ForeignKey,
  "address_line_1" Char,
  "address_line_2" Char,
  "postal_code" Char,
  "city" Char
);

CREATE TABLE "Cart" (
  "id" integer PRIMARY KEY,
  "created_at" DateTime,
  "user" ForeignKey,
  "updated_at" DateTime,
  "history" HistoricalRecords
);

CREATE TABLE "CartItem" (
  "id" integer PRIMARY KEY,
  "cart" ForeignKey,
  "history" HistoricalRecords,
  "product" ForeignKey,
  "created_at" DateTime,
  "updated_at" DateTime,
  "quantity" Integer
);

CREATE TABLE "Discount" (
  "id" integer PRIMARY KEY,
  "history" HistoricalRecords,
  "updated_at" DateTime,
  "created_at" DateTime,
  "type" Char,
  "percentage" Decimal,
  "name" Char
);

CREATE TABLE "DiscountInvoice" (
  "id" integer PRIMARY KEY,
  "history" HistoricalRecords,
  "invoice" ManyToMany,
  "start_date" Date,
  "end_date" Date,
  "percentage" Decimal,
  "name" Char
);

CREATE TABLE "DiscountInvoiceItem" (
  "id" integer PRIMARY KEY,
  "name" Char,
  "percentage" Decimal,
  "start_date" Date,
  "end_date" Date,
  "products" ManyToMany,
  "history" HistoricalRecords
);

CREATE TABLE "InventoryMovement" (
  "id" integer PRIMARY KEY,
  "movement_type" Char,
  "product_stock" ForeignKey,
  "quantity" PositiveInteger,
  "movement_date" DateTime,
  "history" HistoricalRecords
);

CREATE TABLE "Invoice" (
  "id" integer PRIMARY KEY,
  "firstname" Char,
  "history" HistoricalRecords,
  "payment_terms" Char,
  "billing_address_country" Char,
  "shipping_address" Char,
  "shipping_address_city" Char,
  "shipping_address_state" Char,
  "shipping_address_postal_code" Char,
  "shipping_address_country" Char,
  "contact_person" Char,
  "contact_email" Email,
  "registration_number" Char,
  "tax_id" Char,
  "notes" Text,
  "contact_phone" Char,
  "billing_address_postal_code" Char,
  "billing_address_state" Char,
  "billing_address_city" Char,
  "billing_address" Char,
  "invoice_number" Char,
  "date_created" Date,
  "due_date" Date,
  "customer" Char,
  "company_group" Char,
  "company" Char,
  "surname" Char
);

CREATE TABLE "InvoiceItem" (
  "id" integer PRIMARY KEY,
  "total_payable" Decimal,
  "history" HistoricalRecords,
  "product_quantity" Decimal,
  "total_discount" Decimal,
  "total_vat" Decimal,
  "total_price" Decimal,
  "payable" Decimal,
  "discount" Decimal,
  "vat_percentage" Decimal,
  "product_code" Char,
  "product_unit_price" Decimal,
  "product_name" Char
);

CREATE TABLE "Order" (
  "id" integer PRIMARY KEY,
  "created_at" DateTime,
  "billing_address" ForeignKey,
  "user" ForeignKey,
  "order_date" DateTime,
  "total_amount" Decimal,
  "order_status" Char,
  "shipping_address" ForeignKey,
  "payment" ForeignKey,
  "updated_at" DateTime,
  "history" HistoricalRecords
);

CREATE TABLE "OrderItem" (
  "id" integer PRIMARY KEY,
  "order" ForeignKey,
  "product" ForeignKey,
  "price_per_item" Decimal,
  "discount_perc" Decimal,
  "discount_type" Decimal,
  "total_price_after_discount" Decimal,
  "created_at" DateTime,
  "updated_at" DateTime,
  "history" HistoricalRecords,
  "quantity" Integer
);

CREATE TABLE "Payment" (
  "id" integer PRIMARY KEY,
  "updated_at" DateTime,
  "order" ForeignKey,
  "amount" Decimal,
  "payment_method" Char,
  "payment_status" Char,
  "transaction_id" Char,
  "payment_date" DateTime,
  "history" HistoricalRecords,
  "created_at" DateTime
);

CREATE TABLE "Product" (
  "id" integer PRIMARY KEY,
  "name" Char,
  "category" ForeignKey,
  "updated_at" DateTime,
  "is_active" Boolean,
  "available" Boolean,
  "history" HistoricalRecords,
  "description" Text,
  "price" Decimal,
  "stock_quantity" Integer,
  "created_at" DateTime
);

CREATE TABLE "ProductAttribute" (
  "id" integer PRIMARY KEY,
  "product" ForeignKey,
  "attribute" Char,
  "history" HistoricalRecords,
  "value" Char
);

CREATE TABLE "ProductCategory" (
  "id" integer PRIMARY KEY,
  "name" Char,
  "description" Text,
  "parent" ForeignKey,
  "created_at" DateTime,
  "slug" Slug,
  "updated_at" DateTime,
  "history" HistoricalRecords
);

CREATE TABLE "ProductHistory" (
  "id" integer PRIMARY KEY,
  "Action" Char,
  "User" Char,
  "Timestamp" DateTime,
  "Data_before" JSON,
  "Data_after" JSON,
  "history" HistoricalRecords,
  "Product" Char
);

CREATE TABLE "ProductImage" (
  "id" integer PRIMARY KEY,
  "product" ForeignKey,
  "end_date" Date,
  "alt_text" Char,
  "image" Image
);

CREATE TABLE "ProductStock" (
  "id" integer PRIMARY KEY,
  "history" HistoricalRecords,
  "quantity" PositiveInteger,
  "product" OneToOne
);

CREATE TABLE "ProductView" (
  "id" integer PRIMARY KEY,
  "product" Char,
  "timestamp" DateTime,
  "history" HistoricalRecords,
  "data_before" JSON,
  "action" Char,
  "user" Char,
  "data_after" JSON
);

CREATE TABLE "Review" (
  "id" integer PRIMARY KEY,
  "history" HistoricalRecords,
  "created_at" DateTime,
  "product" ForeignKey,
  "review_date" DateTime,
  "comment" Text,
  "rating" Integer,
  "updated_at" DateTime,
  "user" ForeignKey
);

CREATE TABLE "Warehouse" (
  "id" integer PRIMARY KEY,
  "history" HistoricalRecords,
  "location" Char,
  "name" Char
);

CREATE TABLE "CartActivity" (
  "id" integer PRIMARY KEY,
  "activity_type" Char,
  "history" HistoricalRecords,
  "timestamp" DateTime,
  "quantity" Integer,
  "product" ForeignKey,
  "user_session" ForeignKey
);

CREATE TABLE "ClickEvent" (
  "id" integer PRIMARY KEY,
  "timestamp" DateTime,
  "element_id" Char,
  "user_session" ForeignKey,
  "history" HistoricalRecords
);

CREATE TABLE "ErrorLog" (
  "id" integer PRIMARY KEY,
  "timestamp" DateTime,
  "user_session" ForeignKey,
  "error_message" Text
);

CREATE TABLE "Event" (
  "id" integer PRIMARY KEY,
  "details" Text,
  "timestamp" DateTime,
  "event_type" Char,
  "user_session" ForeignKey,
  "history" HistoricalRecords
);

CREATE TABLE "PageView" (
  "id" integer PRIMARY KEY,
  "user_session" ForeignKey,
  "url" URL,
  "timestamp" DateTime,
  "history" HistoricalRecords
);

CREATE TABLE "SearchQuery" (
  "id" integer PRIMARY KEY,
  "history" HistoricalRecords,
  "timestamp" DateTime,
  "user_session" ForeignKey,
  "query" Text
);

CREATE TABLE "UserDevice" (
  "id" integer PRIMARY KEY,
  "history" HistoricalRecords,
  "timestamp" DateTime,
  "device_details" Text,
  "user_session" ForeignKey
);

CREATE TABLE "UserFeedback" (
  "id" integer PRIMARY KEY,
  "timestamp" DateTime,
  "feedback" Text,
  "user_session" ForeignKey
);

CREATE TABLE "UserPreference" (
  "id" integer PRIMARY KEY,
  "user" OneToOne,
  "preferences" JSON,
  "history" HistoricalRecords
);

CREATE TABLE "UserSession" (
  "id" integer PRIMARY KEY,
  "session_key" Char,
  "user" ForeignKey,
  "start_time" DateTime,
  "end_time" DateTime,
  "ip_address" Char,
  "history" HistoricalRecords
);

CREATE TABLE "Wishlist" (
  "id" integer PRIMARY KEY,
  "added_on" DateTime,
  "created_at" DateTime,
  "updated_at" DateTime,
  "history" HistoricalRecords,
  "product" ForeignKey,
  "user" ForeignKey
);

CREATE TABLE "UserProfile" (
  "id" integer PRIMARY KEY,
  "user" OneToOne,
  "phone_number" Char,
  "address_line_1" Char,
  "address_line_2" Char,
  "city" Char,
  "state" Char,
  "country" Char,
  "postal_code" Char,
  "birth_date" Date,
  "history" HistoricalRecords
);

CREATE TABLE "Interaction" (
  "id" integer PRIMARY KEY,
  "customer" ForeignKey,
  "date" DateTime,
  "interaction_type" ForeignKey,
  "notes" Text,
  "history" HistoricalRecords
);

CREATE TABLE "InteractionDetails" (
  "id" integer PRIMARY KEY,
  "handled_by" ForeignKey,
  "interaction" OneToOne,
  "details" Text,
  "history" HistoricalRecords
);

CREATE TABLE "InteractionType" (
  "id" integer PRIMARY KEY,
  "name" Char
);

CREATE TABLE "Task" (
  "id" integer PRIMARY KEY,
  "customer" ForeignKey,
  "task_type" ForeignKey,
  "due_date" DateTime,
  "description" Text,
  "assigned_to" ForeignKey,
  "history" HistoricalRecords
);

CREATE TABLE "TaskType" (
  "id" integer PRIMARY KEY,
  "name" Char,
  "history" HistoricalRecords
);

CREATE TABLE "User" (
  "id" integer PRIMARY KEY
);

ALTER TABLE "Employee" ADD FOREIGN KEY ("employer") REFERENCES "Employer" ("id");

ALTER TABLE "Employee" ADD FOREIGN KEY ("manager") REFERENCES "Manager" ("id");

ALTER TABLE "Employee" ADD FOREIGN KEY ("organization") REFERENCES "Organization" ("id");

ALTER TABLE "Employer" ADD FOREIGN KEY ("organization") REFERENCES "Organization" ("id");

ALTER TABLE "Individual" ADD FOREIGN KEY ("employee") REFERENCES "Employee" ("id");

ALTER TABLE "Individual" ADD FOREIGN KEY ("user") REFERENCES "User" ("id");

ALTER TABLE "Manager" ADD FOREIGN KEY ("employer") REFERENCES "Employer" ("id");

ALTER TABLE "Manager" ADD FOREIGN KEY ("organization") REFERENCES "Organization" ("id");

ALTER TABLE "CustomerUserProfileB2B" ADD FOREIGN KEY ("company") REFERENCES "CustomerB2B" ("id");

ALTER TABLE "Address" ADD FOREIGN KEY ("user") REFERENCES "User" ("id");

ALTER TABLE "Cart" ADD FOREIGN KEY ("user") REFERENCES "User" ("id");

ALTER TABLE "CartItem" ADD FOREIGN KEY ("cart") REFERENCES "Cart" ("id");

ALTER TABLE "CartItem" ADD FOREIGN KEY ("product") REFERENCES "Product" ("id");

ALTER TABLE "DiscountInvoice" ADD FOREIGN KEY ("invoice") REFERENCES "Invoice" ("id");

ALTER TABLE "DiscountInvoiceItem" ADD FOREIGN KEY ("products") REFERENCES "Product" ("id");

ALTER TABLE "InventoryMovement" ADD FOREIGN KEY ("product_stock") REFERENCES "ProductStock" ("id");

ALTER TABLE "Order" ADD FOREIGN KEY ("billing_address") REFERENCES "Address" ("id");

ALTER TABLE "Order" ADD FOREIGN KEY ("user") REFERENCES "User" ("id");

ALTER TABLE "Order" ADD FOREIGN KEY ("shipping_address") REFERENCES "Address" ("id");

ALTER TABLE "Order" ADD FOREIGN KEY ("payment") REFERENCES "Payment" ("id");

ALTER TABLE "OrderItem" ADD FOREIGN KEY ("order") REFERENCES "Order" ("id");

ALTER TABLE "OrderItem" ADD FOREIGN KEY ("product") REFERENCES "Product" ("id");

ALTER TABLE "Payment" ADD FOREIGN KEY ("order") REFERENCES "Order" ("id");

ALTER TABLE "Product" ADD FOREIGN KEY ("category") REFERENCES "ProductCategory" ("id");

ALTER TABLE "ProductAttribute" ADD FOREIGN KEY ("product") REFERENCES "Product" ("id");

ALTER TABLE "ProductCategory" ADD FOREIGN KEY ("parent") REFERENCES "ProductCategory" ("id");

ALTER TABLE "ProductImage" ADD FOREIGN KEY ("product") REFERENCES "Product" ("id");

ALTER TABLE "ProductStock" ADD FOREIGN KEY ("product") REFERENCES "Product" ("id");

ALTER TABLE "Review" ADD FOREIGN KEY ("product") REFERENCES "Product" ("id");

ALTER TABLE "Review" ADD FOREIGN KEY ("user") REFERENCES "User" ("id");

ALTER TABLE "CartActivity" ADD FOREIGN KEY ("product") REFERENCES "Product" ("id");

ALTER TABLE "CartActivity" ADD FOREIGN KEY ("user_session") REFERENCES "UserSession" ("id");

ALTER TABLE "ClickEvent" ADD FOREIGN KEY ("user_session") REFERENCES "UserSession" ("id");

ALTER TABLE "ErrorLog" ADD FOREIGN KEY ("user_session") REFERENCES "UserSession" ("id");

ALTER TABLE "Event" ADD FOREIGN KEY ("user_session") REFERENCES "UserSession" ("id");

ALTER TABLE "PageView" ADD FOREIGN KEY ("user_session") REFERENCES "UserSession" ("id");

ALTER TABLE "SearchQuery" ADD FOREIGN KEY ("user_session") REFERENCES "UserSession" ("id");

ALTER TABLE "UserDevice" ADD FOREIGN KEY ("user_session") REFERENCES "UserSession" ("id");

ALTER TABLE "UserFeedback" ADD FOREIGN KEY ("user_session") REFERENCES "UserSession" ("id");

ALTER TABLE "UserPreference" ADD FOREIGN KEY ("user") REFERENCES "User" ("id");

ALTER TABLE "UserSession" ADD FOREIGN KEY ("user") REFERENCES "User" ("id");

ALTER TABLE "Wishlist" ADD FOREIGN KEY ("product") REFERENCES "Product" ("id");

ALTER TABLE "Wishlist" ADD FOREIGN KEY ("user") REFERENCES "User" ("id");

ALTER TABLE "UserProfile" ADD FOREIGN KEY ("user") REFERENCES "User" ("id");

ALTER TABLE "Interaction" ADD FOREIGN KEY ("customer") REFERENCES "Customer" ("id");

ALTER TABLE "Interaction" ADD FOREIGN KEY ("interaction_type") REFERENCES "InteractionType" ("id");

ALTER TABLE "InteractionDetails" ADD FOREIGN KEY ("handled_by") REFERENCES "User" ("id");

ALTER TABLE "InteractionDetails" ADD FOREIGN KEY ("interaction") REFERENCES "Interaction" ("id");

ALTER TABLE "Task" ADD FOREIGN KEY ("customer") REFERENCES "Customer" ("id");

ALTER TABLE "Task" ADD FOREIGN KEY ("task_type") REFERENCES "TaskType" ("id");

ALTER TABLE "Task" ADD FOREIGN KEY ("assigned_to") REFERENCES "User" ("id");
