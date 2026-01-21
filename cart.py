from utils import load_data, save_data
from datetime import datetime

MEMBERSHIP_RULES = {
    "bronze": {"points": 0.05, "delivery": 50, "discount": 0},
    "silver": {"points": 0.10, "delivery": 50, "discount": 0},
    "gold": {"points": 0.15, "delivery": 0, "discount": 0},
    "business": {"points": 0.20, "delivery": 50, "discount": 0.10}
}

def add_to_cart(user):
    products = load_data("data/products.json")
    pid = input("Enter product ID to add: ")

    for p in products:
        if str(p["id"]) == pid:
            user["cart"].append(p)
            print("Product added to cart")
            return

    print("Product not found")

def view_cart(user):
    if not user["cart"]:
        print("Cart is empty")
        return

    print("\n--- YOUR CART ---")
    total = 0
    for i, p in enumerate(user["cart"], start=1):
        print(f"{i}. {p['name']} - ${p['price']}")
        total += p["price"]

    print(f"Total: ${total}")

def checkout(user):
    if not user["cart"]:
        print("Cart is empty")
        return

    membership = user["membership"]
    rules = MEMBERSHIP_RULES[membership]

    subtotal = sum(p["price"] for p in user["cart"])
    discount = subtotal * rules["discount"]
    subtotal_after_discount = subtotal - discount

    print("\n1. Delivery ($50)")
    print("2. Pick up from store")

    choice = input("Choose delivery method: ")

    if choice == "1":
        delivery_cost = rules["delivery"]
        delivery_method = "delivery"
    elif choice == "2":
        delivery_cost = 0
        delivery_method = "store pickup"
    else:
        print("Invalid option")
        return

    total = subtotal_after_discount + delivery_cost

    print("\n--- ORDER SUMMARY ---")
    print(f"Subtotal: ${subtotal}")
    if discount > 0:
        print(f"Discount: -${discount}")
    print(f"Delivery: ${delivery_cost}")
    print(f"TOTAL: ${total}")
    print(f"Your points: {user['points']}")

    while True:
        use_points = input("Use points? (yes/no): ").lower()
        if use_points == "yes":
            used = min(user["points"], total)
            total -= used
            user["points"] -= used
            print(f"Points used: {used}")
            break
        elif use_points == "no":
            break
        else:
            print("Invalid input")


    earned_points = int(subtotal * rules["points"])
    user["points"] += earned_points

    print(f"Points earned: {earned_points}")
    print(f"Final amount to pay: ${total}")

    # -------- SAVE SALE --------
    sales = load_data("data/sales.json")

    sale = {
        "sale_id": len(sales) + 1,
        "customer_id": user["id"],
        "username": user["username"],
        "items": [
            {"id": p["id"], "name": p["name"], "price": p["price"]}
            for p in user["cart"]
        ],
        "membership": membership,
        "delivery_method": delivery_method,
        "total_paid": total,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    sales.append(sale)
    save_data("data/sales.json", sales)

    print("\nCheckout complete (prototype)")
    user["cart"].clear()

def cart_menu(user):
    while True:
        print("\n--- YOUR CART ---")

        if not user["cart"]:
            print("Cart is empty")
            print("\n1. Back")

            choice = input("Choose: ")
            if choice == "1":
                break
            else:
                print("Invalid choice")
        else:
            view_cart(user)

            print("\n1. Checkout")
            print("2. Back")

            choice = input("Choose: ")

            if choice == "1":
                checkout(user)
            elif choice == "2":
                break
            else:
                print("Invalid choice")