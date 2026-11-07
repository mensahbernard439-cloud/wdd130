"""
Course: CSE 111
Project: Grocery Store Receipt Generator

Exceeding the Requirements:
- Added a "Return By" date calculation to the receipt that displays a date
  30 days in the future at 9:00 PM using datetime and timedelta.
"""

import csv
from datetime import datetime, timedelta


def read_dictionary(filename, key_column_index):
    """Reads product data from a CSV file into a dictionary.

    Parameters:
        filename: path to the CSV file.
        key_column_index: column index to be used as the dictionary key.

    Returns:
        A dictionary where each key maps to a list of values from that row.
    """
    products_dict = {}

    with open(filename, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)

        # Skip the header row
        next(reader)

        for row in reader:
            if row:  # Ensure line is not empty
                key = row[key_column_index]
                products_dict[key] = row

    return products_dict


def main():
    # Tax rate (6%)
    SALES_TAX_RATE = 0.06

    try:
        # 1. Read product catalog into a dictionary (Product ID as key)
        products_dict = read_dictionary("products.csv", 0)

        # Store Header
        print("====================================")
        print("       UNCLE'S GROCERY MARKET       ")
        print("====================================\n")
        print("Order Details:")
        print("------------------------------------")

        total_items_count = 0
        subtotal = 0.0

        # 2. Read customer request CSV file
        with open("request.csv", "r", encoding="utf-8") as request_file:
            reader = csv.reader(request_file)

            # Skip header row
            next(reader)

            # Process each requested item
            for row in reader:
                if not row:
                    continue

                prod_id = row[0]
                quantity = int(row[1])

                # Look up product in catalog (Raises KeyError if ID is not found)
                product_info = products_dict[prod_id]
                item_name = product_info[1]
                item_price = float(product_info[2])

                # Calculate running totals
                total_items_count += quantity
                subtotal += item_price * quantity

                # Print item line on receipt
                print(f"{item_name}: {quantity} @ ${item_price:.2f} each")

        # 3. Calculations
        sales_tax = subtotal * SALES_TAX_RATE
        total_due = subtotal + sales_tax

        # 4. Print Summary & Receipt Footer
        print("------------------------------------")
        print(f"Number of Items: {total_items_count}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax (6%): ${sales_tax:.2f}")
        print(f"Total Due: ${total_due:.2f}")
        print("------------------------------------")

        # Current Date and Time
        current_date_time = datetime.now()
        print(f"\nDate & Time: {current_date_time:%a %b %d %I:%M:%S %Y}")

        # Exceeding Requirements Feature: 30-Day Return Policy
        return_date = (current_date_time + timedelta(days=30)).replace(
            hour=21, minute=0, second=0
        )
        print(f"Return Policy: Return by {return_date:%b %d, %Y by 9:00 PM}")

        print("\nThank you for shopping at Uncle's Grocery Market!")
        print("====================================")

    except FileNotFoundError as file_err:
        print("\n[Error]: Missing File.")
        print(f"Please check that the file exists: {file_err.filename}")

    except PermissionError as perm_err:
        print("\n[Error]: Permission Denied.")
        print(f"Cannot read file: {perm_err.filename}")

    except KeyError as key_err:
        print("\n[Error]: Product Not Found.")
        print(
            f"Product ID {key_err} in request.csv does not exist in products.csv catalog."
        )


if __name__ == "__main__":
    main()