from products import customer_product_menu
from cart import cart_menu
from support import contact_support
from utils import load_data


def show_promotions():
    promotions = load_data("data/promotions.json")

    print("\n--- PROMOTIONS & MEMBERSHIP ---")
    for p in promotions:
        print(f"- {p}")

    input("\nPress Enter to go back...")

def customer_menu(user):
    while True:
        print("\n--- CUSTOMER MENU ---")
        print(f"Membership: {user['membership'].capitalize()} | Points: {user['points']}")
        print("--------------------------------")

        print("1. View products")
        print("2. View promotions & membership")
        print("3. Shopping cart")
        print("4. Purchase history")
        print("5. Contact support")
        print("6. Logout")

        choice = input("Choose: ")

        if choice == "1":
            customer_product_menu(user)

        elif choice == "2":
            show_promotions()

        elif choice == "3":
            cart_menu(user)

        elif choice == "4":
            view_purchase_history(user)

        elif choice == "5":
            contact_support()

        elif choice == "6":
            break

def view_purchase_history(user):
    sales = load_data("data/sales.json")

    print("\n--- YOUR PURCHASE HISTORY ---")
    found = False

    for s in sales:
        if s["customer_id"] == user["id"]:
            found = True
            print(f"\nOrder ID: {s['sale_id']}")
            print(f"Date: {s['date']}")
            print(f"Total paid: ${s['total_paid']}")
            print("Items:")
            for item in s["items"]:
                print(f" - {item['name']} (${item['price']})")

    if not found:
        print("No purchases yet")

    input("\nPress Enter to go back...")
