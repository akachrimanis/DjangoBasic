
		}
            table Employee {
		id primary key 
		first_name Char
		surname Char
		age PositiveInteger
		email Email
		phone Char
		address Char
		department Char
		role Char
		employer ForeignKey
		manager ForeignKey
		organization ForeignKey

		}
            table Employer {
		id primary key 
		company_name Char
		password Char
		email Email
		name Char
		organization ForeignKey
		history HistoricalRecords

		}
            table Individual {
		id primary key 
		history HistoricalRecords
		employee ForeignKey
		user OneToOne

		}
            table Manager {
		id primary key 
		first_name Char
		surname Char
		age PositiveInteger
		email Email
		phone Char
		address Char
		department Char
		role Char
		employer ForeignKey
		organization ForeignKey

		}
            table Organization {
		id primary key 
		name Char
		address Char
		history HistoricalRecords

		}
Ref: Employee.employer > Employer.id 
Ref: Employee.manager > Manager.id 
Ref: Employee.organization > Organization.id 
Ref: Employer.organization > Organization.id 
Ref: Individual.employee > Employee.id 
Ref: Individual.user > User.id 
Ref: Manager.employer > Employer.id 
Ref: Manager.organization > Organization.id 


		}
            table Customer {
		id primary key 
		name Char
		active Boolean
		AFM Integer
		contact_first_name Char
		contact_last_name Char
		email Email
		phone Char
		address Text
		created_at DateTime
		updated_at DateTime
		history HistoricalRecords

		}


		}
            table CustomerB2B {
		id primary key 
		name Char
		history HistoricalRecords
		updated_at DateTime
		created_at DateTime
		notes Text
		company_group Char
		bank_account_number Char
		bank_name Char
		payment_terms Char
		registration_number Char
		tax_id Char
		annual_revenue Decimal
		company_size PositiveInteger
		swift_code Char
		contact_phone Char
		contact_email Email
		contact_person Char
		country Char
		postal_code Char
		state Char
		city Char
		address_line_2 Char
		address_line_1 Char
		website URL
		phone Char
		email Email
		industry Char

		}
            table CustomerB2BAggregate_country {
		id primary key 
		country  Char
		total_customers  Char
		total_industries  Integer
		total_company_size  PositiveInteger
		total_annual_revenue  Decimal

		}
            table CustomerB2BGoup {
		id primary key 
		registration_number Char
		updated_at DateTime
		history HistoricalRecords
		created_at DateTime
		notes Text
		company_group Char
		swift_code Char
		bank_account_number Char
		bank_name Char
		payment_terms Char
		tax_id Char
		city Char
		company_size PositiveInteger
		name Char
		email Email
		phone Char
		annual_revenue Decimal
		address_line_1 Char
		address_line_2 Char
		website URL
		postal_code Char
		country Char
		contact_person Char
		contact_email Email
		contact_phone Char
		industry Char
		state Char

		}
            table CustomerUserProfile {
		id primary key 
		description Char
		company ForeignKey
		username Char
		firstname Char
		surname Char
		email Email
		phone Char
		history HistoricalRecords

		}
Ref: CustomerUserProfile.company > CustomerB2B.id 


		}
            table CustomerB2C {
		id primary key 
		firstname Char
		history HistoricalRecords
		updated_at DateTime
		created_at DateTime
		notes Text
		postal_code Char
		state Char
		city Char
		country Char
		address_line_1 Char
		website URL
		phone Char
		email Email
		date_of_birth Date
		surname Char
		address_line_2 Char

		}
            table CustomerUserProfile {
		id primary key 
		last_login Char
		username Char
		firstname Char
		surname Char
		email Email
		phone Char
		history HistoricalRecords

		}


		}
            table Customer {
		id primary key 
		date DateTime
		price Integer
		created_at DateTime
		updated_at DateTime

		}


		}
            table Address {
		id primary key 
		address_line_2 Char
		history HistoricalRecords
		updated_at DateTime
		created_at DateTime
		address_type Char
		is_billing_address Boolean
		country Char
		postal_code Char
		is_shipping_addrss Boolean
		city Char
		address_id Auto
		user ForeignKey
		state Char
		address_line_1 Char

		}
            table Cart {
		id primary key 
		created_at DateTime
		updated_at DateTime
		history HistoricalRecords
		user ForeignKey
		cart_id Auto

		}
            table CartItem {
		cart_item_id Auto
		cart_item_id Auto primary key 
		created_at DateTime
		history HistoricalRecords
		updated_at DateTime
		cart ForeignKey
		quantity Integer
		product ForeignKey

		}
            table Discount {
		id primary key 
		history HistoricalRecords
		updated_at DateTime
		created_at DateTime
		type Char
		percentage Decimal
		name Char

		}
            table DiscountInvoice {
		id primary key 
		history HistoricalRecords
		invoice ManyToMany
		end_date Date
		percentage Decimal
		name Char
		start_date Date

		}
            table DiscountInvoiceItem {
		id primary key 
		history HistoricalRecords
		start_date Date
		percentage Decimal
		name Char
		products ManyToMany
		end_date Date

		}
            table InventoryMovement {
		id primary key 
		movement_date DateTime
		history HistoricalRecords
		quantity PositiveInteger
		movement_type Char
		product_stock ForeignKey

		}
            table Order {
		order_id Auto
		order_id Auto primary key 
		user ForeignKey
		order_status Char
		total_amount Decimal
		order_date DateTime
		shipping_address ForeignKey
		billing_address ForeignKey
		created_at DateTime
		updated_at DateTime
		payment ForeignKey
		history HistoricalRecords

		}
            table OrderItem {
		id primary key 
		created_at DateTime
		updated_at DateTime
		history HistoricalRecords
		order_item_id Auto
		total_price_after._discount Decimal
		discount_type Decimal
		discount_perc Decimal
		price_per_item Decimal
		quantity Integer
		product ForeignKey
		order ForeignKey

		}
            table Payment {
		id primary key 
		payment_date DateTime
		payment_id Auto
		order ForeignKey
		amount Decimal
		payment_method Char
		payment_status Char
		transaction_id Char
		history HistoricalRecords
		created_at DateTime
		updated_at DateTime

		}
            table Product {
		product_id Auto
		product_id Auto primary key 
		created_at DateTime
		available Boolean
		is_active Boolean
		updated_at DateTime
		category ForeignKey
		history HistoricalRecords
		stock_quantity Integer
		price Decimal
		description Text
		name Char

		}
            table Product History {
		id primary key 
		Product Char

		}
            table ProductAttribute {
		id primary key 
		product ForeignKey
		value Char
		history HistoricalRecords
		attribute Char

		}
            table ProductCategory {
		id primary key 
		created_at DateTime
		parent ForeignKey
		name Char
		category_id Auto
		updated_at DateTime
		description Text
		slug Slug
		history HistoricalRecords

		}
            table ProductHistory {
		id primary key 
		User Char
		history HistoricalRecords
		Timestamp DateTime
		Data_after JSON
		Data_before JSON
		Action Char

		}
            table ProductImage {
		id primary key 
		product ForeignKey
		image Image
		alt_text Char
		end_date Date

		}
            table ProductStock {
		id primary key 
		history HistoricalRecords
		quantity PositiveInteger
		product OneToOne

		}
            table ProductView {
		id primary key 
		history HistoricalRecords
		data_after JSON
		data_before JSON
		action Char
		timestamp DateTime
		user Char
		product Char

		}
            table Review {
		id primary key 
		updated_at DateTime
		review_id Auto
		product ForeignKey
		user ForeignKey
		comment Text
		review_date DateTime
		created_at DateTime
		history HistoricalRecords
		rating Integer

		}
            table Warehouse {
		id primary key 
		name Char
		location Char
		history HistoricalRecords

		}
Ref: Address.user > User.address_id 
Ref: Cart.user > User.address_id 
Ref: CartItem.cart > Cart.cart_item_id 
Ref: CartItem.product > Product.cart_item_id 
Ref: DiscountInvoice.invoice > Invoice.cart_item_id 
Ref: DiscountInvoiceItem.products > Product.cart_item_id 
Ref: InventoryMovement.product_stock > ProductStock.cart_item_id 
Ref: Order.user > User.order_id 
Ref: Order.shipping_address > Address.order_id 
Ref: Order.billing_address > Address.order_id 
Ref: Order.payment > Payment.order_id 
Ref: OrderItem.product > Product.order_item_id 
Ref: OrderItem.order > Order.order_item_id 
Ref: Payment.order > Order.payment_id 
Ref: Product.category > Category.product_id 
Ref: ProductAttribute.product > Product.product_id 
Ref: ProductCategory.parent > self.product_id 
Ref: ProductImage.product > Product.category_id 
Ref: ProductStock.product > Product.category_id 
Ref: Review.product > Product.review_id 
Ref: Review.user > User.review_id 


		}
            table CartActivity {
		id primary key 
		user_session ForeignKey
		history HistoricalRecords
		timestamp DateTime
		quantity Integer
		product ForeignKey
		activity_type Char

		}
            table ClickEvent {
		id primary key 
		timestamp DateTime
		element_id Char
		user_session ForeignKey
		history HistoricalRecords

		}
            table ErrorLog {
		id primary key 
		timestamp DateTime
		user_session ForeignKey
		error_message Text

		}
            table Event {
		id primary key 
		timestamp DateTime
		event_type Char
		user_session ForeignKey
		details Text

		}
            table PageView {
		id primary key 
		user_session ForeignKey
		url URL
		timestamp DateTime
		history HistoricalRecords

		}
            table SearchQuery {
		id primary key 
		history HistoricalRecords
		timestamp DateTime
		query Text
		user_session ForeignKey

		}
            table UserDevice {
		id primary key 
		timestamp DateTime
		device_details Text
		user_session ForeignKey

		}
            table UserFeedback {
		id primary key 
		timestamp DateTime
		feedback Text
		user_session ForeignKey

		}
            table UserPreference {
		id primary key 
		user OneToOne
		preferences JSON
		history HistoricalRecords

		}
            table UserSession {
		id primary key 
		session_key Char
		history HistoricalRecords
		user ForeignKey
		end_time DateTime
		ip_address Char
		history HistoricalRecords
		history HistoricalRecords
		start_time DateTime

		}
            table Wishlist {
		id primary key 
		product ForeignKey
		added_on DateTime
		created_at DateTime
		updated_at DateTime
		history HistoricalRecords
		user ForeignKey

		}
Ref: CartActivity.user_session > UserSession.id 
Ref: CartActivity.product > Product.id 
Ref: ClickEvent.user_session > UserSession.id 
Ref: ErrorLog.user_session > UserSession.id 
Ref: Event.user_session > UserSession.id 
Ref: PageView.user_session > UserSession.id 
Ref: SearchQuery.user_session > UserSession.id 
Ref: UserDevice.user_session > UserSession.id 
Ref: UserFeedback.user_session > UserSession.id 
Ref: UserPreference.user > User.id 
Ref: UserSession.user > User.id 
Ref: Wishlist.product > Product.id 
Ref: Wishlist.user > User.id 


		}
            table UserProfile {
		id primary key 
		user OneToOne
		phone_number Char
		address_line_1 Char
		address_line_2 Char
		city Char
		state Char
		country Char
		postal_code Char
		birth_date Date

		}
Ref: UserProfile.user > User.id 


		}
            table Interaction {
		id primary key 
		customer ForeignKey
		date DateTime
		interaction_type ForeignKey
		notes Text
		history HistoricalRecords

		}
            table InteractionDetails {
		id primary key 
		handled_by ForeignKey
		interaction OneToOne
		details Text
		history HistoricalRecords

		}
            table InteractionType {
		id primary key 
		name Char

		}
            table Task {
		id primary key 
		customer ForeignKey
		task_type ForeignKey
		due_date DateTime
		description Text
		assigned_to ForeignKey
		history HistoricalRecords

		}
            table TaskType {
		id primary key 
		name Char
		history HistoricalRecords

		}
Ref: Interaction.customer > Customer.id 
Ref: Interaction.interaction_type > InteractionType.id 
Ref: InteractionDetails.handled_by > User.id 
Ref: InteractionDetails.interaction > Interaction.id 
Ref: Task.customer > Customer.id 
Ref: Task.task_type > TaskType.id 
Ref: Task.assigned_to > User.id 


