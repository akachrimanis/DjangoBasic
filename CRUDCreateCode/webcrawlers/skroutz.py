import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.skroutz.gr/"

# Send a GET request to the URL
# Define a custom User-Agent string
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Send a GET request to the URL with custom headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all product categories
    categories = soup.find_all("a", class_="primary-nav__link")
    
    # Extract category names
    category_names = [category.text.strip() for category in categories]
    
    # Find all product names
    products = soup.find_all("div", class_="js-product-list-item")
    
    # Extract product names
    product_names = [product.find("a", class_="js-product-title").text.strip() for product in products]
    
    # Print the results
    print("Product Categories:")
    for category in category_names:
        print(category)
        
    print("\nProduct Names:")
    for product in product_names:
        print(product)
else:
    print("Failed to retrieve the webpage")
