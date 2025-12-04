import csv
import sys


PRODUCTS_FILE = "products.csv"
REQUESTS_FILE = "request.csv"
PRODUCT_NUM_INDEX = 0


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

        print("All Products")
        print(products_dict)
        print("-" * 20)

        print("Requested Items")
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
                product_price = product_info[2]

                print(
                    f"{product_name}: {requested_quantity} @ {product_price}"
                )

    except FileNotFoundError as ex:
        print(f"Error: missing file\n{ex}", file=sys.stderr)
    except PermissionError as ex:
        print(f"Error: permission denied\n{ex}", file=sys.stderr)
    except KeyError as ex:
        print(f"Error: unknown product ID in the request.csv file\n{ex}", file=sys.stderr)
    except IndexError as ex:
        print(f"Error: invalid data format in CSV file\n{ex}", file=sys.stderr)


if __name__ == "__main__":
    main()