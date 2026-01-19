from auth import login, register_customer
from admin_menu import admin_menu
from customer_menu import customer_menu
from support import contact_support

def main():
    while True:
        print("\n--- TECH HOUSE ---")
        print("1. Login")
        print("2. Register")
        print("3. Contact support")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            user = login()
            if user:
                if user["role"] == "administrator":
                    admin_menu(user)
                else:
                    customer_menu(user)

        elif choice == "2":
            register_customer()

        elif choice == "3":
            contact_support()

        elif choice == "4":
            break

main()