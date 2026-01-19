from auth import add_user_by_admin
from products import admin_product_menu
from auth import manage_user_membership, remove_user_points
from utils import load_data

def admin_menu(user):
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Show & manage products")
        print("2. Add administrator / user")
        print("3. Manage user membership")
        print("4. Remove user points")
        print("5. View all sales")
        print("6. Logout")

        choice = input("Choose: ")

        if choice == "1":
            admin_product_menu()
        elif choice == "2":
            add_user_by_admin()
        elif choice == "3":
            manage_user_membership()
        elif choice == "4":
            remove_user_points()
        elif choice == "5":
            view_all_sales()
        elif choice == "6":
            break

def view_all_sales():
    sales = load_data("data/sales.json")

    print("\n--- ALL SALES ---")

    if not sales:
        print("No sales recorded")
        return

    for s in sales:
        print(f"\nSale ID: {s['sale_id']}")
        print(f"Customer: {s['username']} (ID {s['customer_id']})")
        print(f"Date: {s['date']}")
        print(f"Membership: {s['membership']}")
        print(f"Delivery: {s['delivery_method']}")
        print(f"Total paid: ${s['total_paid']}")