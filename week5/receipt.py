import csv
import sys
from datetime import datetime


PRODUCTS_FILE = "products.csv"
REQUESTS_FILE = "request.csv"
PRODUCT_NUM_INDEX = 0
SALES_TAX_RATE = 0.06
STORE_NAME = "Inkom Emporium"


def read_dictionary(filename, key_column_index):
    dictionary = {}
    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[key_column_index]
                    dictionary[key] = row_list
    except FileNotFoundError:
        raise
    except PermissionError:
        raise
        
    return dictionary


def main():
    try:
        products_dict = read_dictionary(PRODUCTS_FILE, PRODUCT_NUM_INDEX)
        
        total_items = 0
        subtotal = 0.0

        print(STORE_NAME)
        print("-" * 20)

        with open(REQUESTS_FILE, "rt") as requests_file:
            reader = csv.reader(requests_file)
            next(reader)

            for request_row in reader:
                if len(request_row) == 0:
                    continue

                product_num = request_row[0]
                requested_quantity = int(request_row[1])

                product_info = products_dict[product_num]

                product_name = product_info[1]
                product_price = float(product_info[2])

                line_cost = requested_quantity * product_price

                print(
                    f"{product_name}: {requested_quantity} @ {product_price:.2f}"
                )

                total_items += requested_quantity
                subtotal += line_cost

        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax

        print("-" * 20)
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")

        print("\nThank you for shopping at the " + STORE_NAME + ".")

        current_date_and_time = datetime.now()
        print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))


    except FileNotFoundError as ex:
        print(f"Error: missing file\n{ex}", file=sys.stderr)
    except PermissionError as ex:
        print(f"Error: permission denied\n{ex}", file=sys.stderr)
    except KeyError as ex:
        print(f"Error: unknown product ID in the request.csv file\n{ex}", file=sys.stderr)
    except IndexError as ex:
        print(f"Error: invalid data format in CSV file\n{ex}", file=sys.stderr)
    except ValueError as ex:
        print(f"Error: non-numeric value found where a number was expected.\n{ex}", file=sys.stderr)


if __name__ == "__main__":
    main()