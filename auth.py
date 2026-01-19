from utils import load_data, save_data

USERS_PATH = "data/users.json"

def login():
    users = load_data(USERS_PATH)

    if not isinstance(users, list):
        print("ERROR: users.json is corrupted")
        return None

    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if not isinstance(user, dict):
            continue

        if user["username"] == username and user["password"] == password:
            user.setdefault("cart", [])
            user.setdefault("membership", "bronze")
            user.setdefault("points", 0)
            print("Login successful")
            return user

    print("Invalid username or password")
    return None

def register_customer():
    users = load_data(USERS_PATH)

    username = input("Choose username: ")
    password = input("Choose password: ")

    new_user = {
        "id": len(users) + 1,
        "username": username,
        "password": password,
        "role": "customer"
    }

    users.append(new_user)
    save_data(USERS_PATH, users)

    print("Customer registered successfully")

def add_user_by_admin():
    users = load_data(USERS_PATH)

    username = input("New username: ")
    password = input("Password: ")
    role = input("Role (administrator/customer): ").lower()

    if role not in ["administrator", "customer"]:
        print("Invalid role")
        return

    new_user = {
        "id": len(users) + 1,
        "username": username,
        "password": password,
        "role": role
    }

    users.append(new_user)
    save_data(USERS_PATH, users)

    print("User added successfully")

def manage_user_membership():
    users = load_data("data/users.json")

    identifier = input("Enter username or user ID: ")

    for user in users:
        if user["username"] == identifier or str(user["id"]) == identifier:
            print(f"Current membership: {user.get('membership', 'bronze')}")
            print("1. bronze\n2. silver\n3. gold\n4. business")

            choice = input("Choose membership: ")
            memberships = ["bronze", "silver", "gold", "business"]

            if choice in ["1", "2", "3", "4"]:
                user["membership"] = memberships[int(choice) - 1]
                save_data("data/users.json", users)
                print("Membership updated")
            return

    print("User not found")

def remove_user_points():
    users = load_data("data/users.json")
    identifier = input("Enter username or user ID: ")

    for user in users:
        if user["username"] == identifier or str(user["id"]) == identifier:
            print(f"Current points: {user['points']}")
            user["points"] = 0
            save_data("data/users.json", users)
            print("Points removed")
            return

    print("User not found")


