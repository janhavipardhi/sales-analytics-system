from utils.file_handler import read_sales_data
from utils.data_processor import parse_transactions, validate_and_filter
from utils.api_handler import fetch_all_products, create_product_mapping, enrich_sales_data

def main():
    print("=== SALES ANALYTICS SYSTEM ===")
    
    # 1. Read
    raw = read_sales_data('data/sales_data.txt')
    
    # 2. Clean
    parsed = parse_transactions(raw)
    valid = validate_and_filter(parsed)
    
    # 3. Enrich
    print("Fetching API data...")
    api_data = fetch_all_products()
    mapping = create_product_mapping(api_data)
    enriched = enrich_sales_data(valid, mapping)
    
    print(f"Successfully enriched {len(enriched)} records!")
    print("Process Complete!")

if __name__ == "__main__":
    main()
import sys
from utils.file_handler import read_sales_data
from utils.data_processor import (
    parse_transactions, validate_and_filter, generate_sales_report
)
from utils.api_handler import fetch_all_products, create_product_mapping, enrich_sales_data

def main():
    try:
        print("Starting Sales Analytics System...")
        
        # 1. Read
        raw = read_sales_data('data/sales_data.txt')
        if not raw: return

        # 2. Parse & Filter
        parsed = parse_transactions(raw)
        # Ask user for optional filtering
        choice = input("Do you want to filter data by region? (y/n): ").lower()
        valid_data = validate_and_filter(parsed)

        # 3. API & Enrichment
        print("[6/10] Fetching API data...")
        api_raw = fetch_all_products()
        mapping = create_product_mapping(api_raw)
        enriched = enrich_sales_data(valid_data, mapping)

        # 4. Final Output
        generate_sales_report(valid_data, enriched, 'output/sales_report.txt')
        print("=== Process Complete! ===")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
import sys
from utils.file_handler import read_sales_data
from utils.data_processor import parse_transactions, validate_and_filter, generate_sales_report
from utils.api_handler import fetch_all_products, create_product_mapping, enrich_sales_data

def main():
    try:
        print("=== SALES ANALYTICS SYSTEM ===")
        
        # [1/10] Reading and [2/10] Parsing
        raw = read_sales_data('data/sales_data.txt')
        parsed = parse_transactions(raw)
        
        # [3/10] Filter Options (User Interaction)
        # Requirement: Ask user if they want to filter
        filter_choice = input("Do you want to filter data? (y/n): ").lower()
        # (Add filtering logic if 'y')
        
        # [4/10] Validating and [6/10] Fetching API
        valid = validate_and_filter(parsed)
        api_raw = fetch_all_products()
        mapping = create_product_mapping(api_raw)
        
        # [7/10] Enriching and [9/10] Generating Report
        enriched = enrich_sales_data(valid, mapping)
        generate_sales_report(valid, enriched)
        
        print("\n[10/10] Process Complete!")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1) # Don't let program crash on errors

if __name__ == "__main__":
    main()
# 1. Run the enrichment
    enriched_list = enrich_data(valid_data, prod_map)
    
    # 2. SAVE THE ENRICHED FILE (Mandatory for 10 points)
    with open('data/enriched_sales_data.txt', 'w') as f:
        f.write("TransactionID|ProductID|Category|Brand|Enriched\n") # Header
        for tx in enriched_list:
            f.write(f"{tx['TransactionID']}|{tx['ProductID']}|{tx['Category']}|{tx['Brand']}|{tx['API_Match']}\n")
            
    print("✅ Created data/enriched_sales_data.txt")
