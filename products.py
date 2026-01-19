from utils import load_data, save_data
from cart import add_to_cart


PRODUCTS_PATH = "data/products.json"


def show_all_products():
    products = load_data(PRODUCTS_PATH)
    print("\n--- PRODUCTS ---")
    for p in products:
        print(f"ID: {p['id']} | {p['name']} | {p['category']} | ${p['price']} | {p['status']}")


def search_products_by_name_or_id():
    products = load_data(PRODUCTS_PATH)
    query = input("Enter product name or ID: ").lower()

    found = False
    for p in products:
        if query == str(p["id"]) or query in p["name"].lower():
            print(f"ID: {p['id']} | {p['name']} | ${p['price']}")
            found = True

    if not found:
        print("No product found")


def view_product_details():
    products = load_data(PRODUCTS_PATH)
    pid = input("Enter product ID: ")

    for p in products:
        if str(p["id"]) == pid:
            print("\n--- PRODUCT DETAILS ---")
            print(f"Name: {p['name']}")
            print(f"Category: {p['category']}")
            print(f"Price: ${p['price']}")
            print(f"Status: {p['status']}")
            return

    print("Product not found")


# ---------------- ADMIN FUNCTIONS ---------------- #

def add_product():
    products = load_data(PRODUCTS_PATH)

    name = input("Product name: ")
    category = input("Category: ")
    price = float(input("Price: "))

    new_product = {
        "id": len(products) + 1,
        "name": name,
        "category": category,
        "price": price,
        "status": "available"
    }

    products.append(new_product)
    save_data(PRODUCTS_PATH, products)
    print("Product added successfully")


def edit_product():
    products = load_data(PRODUCTS_PATH)
    pid = input("Enter product ID to edit: ")

    for p in products:
        if str(p["id"]) == pid:
            print("Leave blank to keep current value")

            name = input(f"Name ({p['name']}): ") or p["name"]
            category = input(f"Category ({p['category']}): ") or p["category"]
            price_input = input(f"Price ({p['price']}): ")

            price = float(price_input) if price_input else p["price"]

            p["name"] = name
            p["category"] = category
            p["price"] = price

            save_data(PRODUCTS_PATH, products)
            print("Product updated")
            return

    print("Product not found")


def admin_product_menu():
    while True:
        print("\n--- ADMIN PRODUCT MENU ---")
        print("1. Show all products")
        print("2. Add product")
        print("3. Edit product")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":
            show_all_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            edit_product()
        elif choice == "4":
            break


def filter_by_category():
    products = load_data(PRODUCTS_PATH)

    categories = [
        "Kitchen appliances",
        "Cleaning devices",
        "Heating and cooling devices",
        "Personal care devices",
        "Smart home devices"
    ]

    print("\n--- CATEGORIES ---")
    for i, c in enumerate(categories, start=1):
        print(f"{i}. {c}")
    print("6. Back")

    choice = input("Choose category: ")

    if choice == "6":
        return

    if not choice.isdigit() or int(choice) < 1 or int(choice) > 5:
        print("Invalid choice")
        return

    selected_category = categories[int(choice) - 1]

    print(f"\n--- {selected_category.upper()} ---")
    found = False
    for p in products:
        if p["category"] == selected_category:
            print(f"ID: {p['id']} | {p['name']} | ${p['price']}")
            found = True

    if not found:
        print("No products in this category")

# ---------------- CUSTOMER FUNCTIONS ---------------- #

def customer_product_menu(user):
    while True:
        print("\n--- PRODUCTS ---")
        print("1. View all products")
        print("2. Search product")
        print("3. Filter by category")
        print("4. View product details")
        print("5. Add product to cart")
        print("6. Back")

        choice = input("Choose: ")

        if choice == "1":
            show_all_products()
        elif choice == "2":
            search_products_by_name_or_id()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            view_product_details()
        elif choice == "5":
            add_to_cart(user)
        elif choice == "6":
            break