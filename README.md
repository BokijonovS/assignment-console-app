# 🛒 Tech House – E-Commerce Prototype (Python)

## 📌 Project Overview
Tech House is a Python-based e-commerce software prototype developed for a home appliance seller.
The application simulates a real shopping system where customers can browse products, manage a shopping cart,
place orders, and earn membership points, while administrators manage users, products, and sales.

This project is an educational prototype and does not process real payments.

---

## 🎯 Project Objectives
- Apply computational thinking and programming principles
- Design and build a functional software solution
- Implement role-based user access (Administrator and Customer)
- Simulate real-world e-commerce behavior using Python

---

## 👤 User Roles

### Administrator
- Add new users (customers or administrators)
- Assign and update user memberships
- Remove user points
- Add, edit, and view products
- View full sales history

### Customer
- View products by category
- Search products by name or ID
- View product details and prices
- Add products to a personal shopping cart
- Choose delivery or store pickup
- Earn and use membership points
- View personal purchase history
- Contact support

---

## 🏷️ Membership System

| Membership | Benefits |
|------------|----------|
| Bronze     | Earns 5% points from total purchase |
| Silver     | Earns 10% points and priority support |
| Gold       | Earns 15% points and free delivery |
| Business   | Earns 20% points and 10% checkout discount |

Notes:
- 1 point equals 1 unit of currency
- Points can be used to reduce or fully cover an order
- Memberships and points are managed by administrators

---

## 🛍️ Product Categories
- Kitchen appliances
- Cleaning devices
- Heating and cooling devices
- Personal care devices
- Smart home devices

---

## 🗂️ Data Storage
The system uses JSON files as a simple database:
- users.json – users, roles, memberships, points, carts
- products.json – product information
- sales.json – completed orders
- promotions.json – membership and promotion information

---

## 📁 Project Structure
## 📁 Project Structure

```text
tech_house_app/
├── main.py
├── auth.py
├── admin_menu.py
├── customer_menu.py
├── products.py
├── cart.py
├── support.py
├── utils.py
└── data/
    ├── users.json
    ├── products.json
    ├── promotions.json
    └── sales.json
---

## ▶️ How to Run the Project
1. Make sure Python is installed
2. Open the project folder
3. Run the application using:

``python main.py``

---

## 🔐 Default Administrator Account
For testing purposes, a default administrator account is included:

Username: admin  
Password: admin123  

This account can be modified or removed in data/users.json.

---

## ⚠️ Important Notes
- This is a prototype, not a production system
- No real payments are processed
- Product stock quantity is not reduced
- The project is intended for educational purposes

---

## 🧠 Skills Demonstrated
- Python programming
- Modular program design
- File handling with JSON
- Role-based access control
- Business logic implementation
- User experience considerations

---

## 👨‍💻 Author
Sanatbek Bokijonov  
Junior Developer / IT Student