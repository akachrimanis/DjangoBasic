import math
import os
BASIC_PATH = os.path.join(os.getcwd(),"CRUDCreateCode") # create template script

# CustomerB2B
num_CustomerB2B = 100 # number of customers to create
num_CustomerUserProfileB2B = num_CustomerB2B

# CustomerB2C
num_CustomerB2C = 100
num_CustomerUserProfileB2C = num_CustomerB2C

# Product
num_Product = 100 # number of products

start_probability = []
transition_matrix_probabilities =[] # transition matrix for customer journey
emmission_probabilities = []
website_interaction_states_declaration = interactions = [
    "Visiting the homepage",
    "Searching for a product",
    "Viewing a product",
    "Adding a product to the shopping cart",
    "Removing a product from the shopping cart",
    "Adjusting the quantity of a product in the shopping cart",
    "Starting the checkout process",
    "Entering shipping information",
    "Entering payment information",
    "Placing an order",
    "Applying a discount code",
    "Leaving a product review",
    "Contacting customer support",
    "Signing up for an account",
    "Logging in to an account",
    "Logging out of an account",
    "Viewing order history",
    "Managing account settings",
    "Exploring product categories",
    "Browsing recommended products",
    "Adding a product to the wishlist",
    "Sharing a product on social media",
    "Participating in a loyalty program",
    "Participating in a referral program",
    "Subscribing to email newsletters",
    "Participating in a survey or poll",
    "Providing feedback or suggestions"
]


order_state_declaration = ['order_made','order_in_preparation', 'order_ready_to_send', 'order_send', 'order_received', 'order_validated', 'order_review']

n = 20  # Change the value of n as needed
discount_list = [round(i * 0.05,2) for i in range(1, n+1)]
campaign_types = ['discount_' + str(i) for i in discount_list]
campaign_types.extend(['take 2 pay 1', 'take 3 pay 2', 'take 1 second half price', 'Sale', 'Discount', 'Clearance', 'Promotion', 'Deal', 'Special Offer'])
campaign_types.extend(["Percentage Discount",
    "Fixed Amount Discount",
    "Buy One Get One (BOGO)",
    "Buy One Get One Free (BOGOF)",
    "Multi-Buy Discount",
    "Bundle Discount",
    "Tiered Discount",
    "Seasonal/Holiday Discount",
    "Clearance/Sale Discount",
    "Loyalty/Rewards Discount",
    "Coupon Code Discount"])
print(campaign_types)

