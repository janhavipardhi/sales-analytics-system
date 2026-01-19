import requests

def fetch_all_products():
    """Fetches up to 100 products from the API."""
    url = "https://dummyjson.com/products?limit=100"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json().get('products', [])
    except:
        return []
    return []

def create_product_mapping(api_products):
    """Creates a dictionary for fast lookup by ID."""
    return {p['id']: p for p in api_products}

def enrich_sales_data(transactions, mapping):
    """Enriches transactions with API data."""
    for tx in transactions:
        # Extract number from P101 -> 101
        prod_id = int(re.search(r'\d+', tx['ProductID']).group())
        if prod_id in mapping:
            tx['API_Category'] = mapping[prod_id].get('category')
            tx['API_Brand'] = mapping[prod_id].get('brand')
            tx['API_Rating'] = mapping[prod_id].get('rating')
            tx['API_Match'] = True
        else:
            tx['API_Category'] = tx['API_Brand'] = tx['API_Rating'] = None
            tx['API_Match'] = False
    return transactions