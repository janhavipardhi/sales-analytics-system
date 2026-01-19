def read_sales_data(filename):
    """Reads sales data and handles encoding issues."""
    encodings = ['utf-8', 'latin-1', 'cp1252']
    for enc in encodings:
        try:
            with open(filename, 'r', encoding=enc) as file:
                # Skip header and remove empty lines
                lines = [line.strip() for line in file.readlines()[1:] if line.strip()]
                return lines
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
            return []
    return []