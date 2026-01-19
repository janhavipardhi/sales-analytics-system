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