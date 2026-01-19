# Sales Analytics System

## Description
A Python-based data pipeline that reads messy sales data, cleans it, enriches it using the DummyJSON API, and generates a business report.

## How to Run
1. Install requirements: `pip install requests`
2. Run the program: `python3 main.py`

## Features
- Handles multiple file encodings (UTF-8, Latin-1).
- Validates data (Removes negative quantities and invalid IDs).
- Connects to External API for product details.
- Generates a 8-section summary report.
