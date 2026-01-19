import re

def parse_transactions(raw_lines):
    """Turns pipe-delimited strings into a list of dictionaries."""
    parsed = []
    for line in raw_lines:
        parts = line.split('|')
        if len(parts) != 8: continue
        try:
            parsed.append({
                'TransactionID': parts[0].strip(),
                'Date': parts[1].strip(),
                'ProductID': parts[2].strip(),
                'ProductName': parts[3].replace(',', '').strip(),
                'Quantity': int(parts[4].replace(',', '').strip()),
                'UnitPrice': float(parts[5].replace(',', '').strip()),
                'CustomerID': parts[6].strip(),
                'Region': parts[7].strip()
            })
        except ValueError: continue
    return parsed

def validate_and_filter(transactions):
    """Applies assignment validation rules."""
    valid = []
    for tx in transactions:
        if (tx['Quantity'] > 0 and tx['UnitPrice'] > 0 and 
            tx['TransactionID'].startswith('T') and 
            tx['ProductID'].startswith('P') and 
            tx['CustomerID'].startswith('C')):
            valid.append(tx)
            
    # Requirement: Print the specific summary
    print(f"Total records parsed: {len(transactions)}")
    print(f"Invalid records removed: {len(transactions) - len(valid)}")
    print(f"Valid records after cleaning: {len(valid)}")
    return valid
from datetime import datetime

def perform_analysis(transactions):
    """Calculates all metrics required for the 8 report sections."""
    # 1. Total Revenue
    total_rev = sum(t['Quantity'] * t['UnitPrice'] for t in transactions)
    
    # 2. Region-wise Performance
    regions = {}
    for t in transactions:
        reg = t['Region']
        amt = t['Quantity'] * t['UnitPrice']
        if reg not in regions:
            regions[reg] = {'sales': 0, 'count': 0}
        regions[reg]['sales'] += amt
        regions[reg]['count'] += 1
    
    # 3. Daily Sales Trend
    trends = {}
    for t in transactions:
        date = t['Date']
        amt = t['Quantity'] * t['UnitPrice']
        if date not in trends:
            trends[date] = {'rev': 0, 'tx': 0, 'custs': set()}
        trends[date]['rev'] += amt
        trends[date]['tx'] += 1
        trends[date]['custs'].add(t['CustomerID'])
    
    # 4. Product Performance (Top 5)
    prod_stats = {}
    for t in transactions:
        name = t['ProductName']
        if name not in prod_stats:
            prod_stats[name] = {'qty': 0, 'rev': 0}
        prod_stats[name]['qty'] += t['Quantity']
        prod_stats[name]['rev'] += t['Quantity'] * t['UnitPrice']
    
    top_products = sorted(prod_stats.items(), key=lambda x: x[1]['qty'], reverse=True)[:5]
    
    return {
        'total_rev': total_rev,
        'regions': regions,
        'trends': dict(sorted(trends.items())),
        'top_products': top_products
    }
