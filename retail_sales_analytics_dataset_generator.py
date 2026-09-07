"""
retail_sales_analytics_dataset_generator.py
Generates realistic relational CSV datasets (with ~5-10% dirty data)
for a Retail Sales Analytics Platform project.

Run: python retail_sales_analytics_dataset_generator.py
Output: ./output/*.csv
"""

import os
import csv
import random
from datetime import datetime, timedelta

random.seed(7)

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2024, 12, 31)

INDIAN_FIRST_NAMES = ["Aarav","Vivaan","Aditya","Vihaan","Arjun","Sai","Reyansh","Ayaan","Krishna","Ishaan",
    "Ananya","Diya","Aadhya","Saanvi","Anika","Myra","Pari","Riya","Isha","Kavya",
    "Rohan","Karan","Nikhil","Rahul","Amit","Sanjay","Deepak","Manish","Suresh","Ramesh",
    "Priya","Neha","Pooja","Sneha","Divya","Shreya","Kritika","Meera","Sunita","Anjali"]

INDIAN_LAST_NAMES = ["Sharma","Verma","Gupta","Iyer","Nair","Reddy","Patel","Mehta","Singh","Kumar",
    "Agarwal","Bansal","Chopra","Malhotra","Rao","Pillai","Joshi","Desai","Kapoor","Bhatt"]

INDIAN_CITIES = ["Mumbai","Delhi","Bengaluru","Hyderabad","Ahmedabad","Chennai","Kolkata","Pune",
    "Jaipur","Surat","Lucknow","Kanpur","Nagpur","Indore","Bhopal","Patna","Vadodara","Ludhiana",
    "Agra","Nashik"]

STATES_BY_CITY = {"Mumbai":"Maharashtra","Delhi":"Delhi","Bengaluru":"Karnataka","Hyderabad":"Telangana",
    "Ahmedabad":"Gujarat","Chennai":"Tamil Nadu","Kolkata":"West Bengal","Pune":"Maharashtra",
    "Jaipur":"Rajasthan","Surat":"Gujarat","Lucknow":"Uttar Pradesh","Kanpur":"Uttar Pradesh",
    "Nagpur":"Maharashtra","Indore":"Madhya Pradesh","Bhopal":"Madhya Pradesh","Patna":"Bihar",
    "Vadodara":"Gujarat","Ludhiana":"Punjab","Agra":"Uttar Pradesh","Nashik":"Maharashtra"}

COMPANY_WORDS1 = ["Bharat","Shree","Om","Royal","National","Sunrise","Silver","Golden","Prime","Trident"]
COMPANY_WORDS2 = ["Traders","Distributors","Enterprises","Industries","Wholesale","Supplies","Impex","Mart"]
COMPANY_SUFFIX = ["Pvt Ltd","LLP","& Co","Group","Industries"]

STORE_TYPES = ["Flagship","Mall Outlet","Standalone","Franchise","Kiosk"]
PAYMENT_METHODS = ["Credit Card","Debit Card","UPI","Cash","Net Banking","Wallet"]
ORDER_STATUS = ["Completed","Cancelled","Returned","Pending"]
CUSTOMER_SEGMENTS = ["Regular","Premium","VIP","New"]
GENDERS = ["Male","Female","Other"]
MOVEMENT_TYPES = ["IN","OUT"]

CATEGORY_NAMES = ["Groceries","Electronics","Apparel","Footwear","Home & Kitchen","Beauty & Personal Care",
    "Sports & Fitness","Toys & Games","Books & Stationery","Furniture","Mobile Accessories",
    "Kitchen Appliances","Bakery","Beverages","Health & Wellness"]

PRODUCT_ADJ = ["Premium","Classic","Deluxe","Eco","Smart","Compact","Pro","Essential","Royal","Ultra"]
PRODUCT_NOUN_BY_CAT = {
    "Groceries": ["Basmati Rice 5kg","Wheat Flour 10kg","Cooking Oil 1L","Sugar 1kg","Toor Dal 1kg","Salt 1kg"],
    "Electronics": ["LED TV 43in","Bluetooth Speaker","Power Bank 10000mAh","Wireless Mouse","USB Cable"],
    "Apparel": ["Cotton Shirt","Denim Jeans","Kurta Set","Formal Trousers","Printed T-Shirt"],
    "Footwear": ["Running Shoes","Leather Sandals","Casual Sneakers","Formal Shoes","Flip Flops"],
    "Home & Kitchen": ["Non-Stick Pan","Steel Dinner Set","Storage Container Set","Pressure Cooker"],
    "Beauty & Personal Care": ["Face Wash","Herbal Shampoo","Body Lotion","Sunscreen SPF50"],
    "Sports & Fitness": ["Yoga Mat","Dumbbell Set","Cricket Bat","Football","Resistance Band"],
    "Toys & Games": ["Building Blocks Set","Remote Control Car","Puzzle 500pc","Board Game"],
    "Books & Stationery": ["Notebook Pack","Ball Pen Set","Sketch Book","Story Book"],
    "Furniture": ["Study Table","Plastic Chair","Bookshelf","Bed Side Table"],
    "Mobile Accessories": ["Phone Case","Tempered Glass","Charging Cable","Earphones"],
    "Kitchen Appliances": ["Mixer Grinder","Electric Kettle","Induction Cooktop","Toaster"],
    "Bakery": ["Whole Wheat Bread","Chocolate Cake","Cookies Pack","Muffins Box"],
    "Beverages": ["Green Tea Pack","Instant Coffee Jar","Fruit Juice 1L","Soft Drink 2L"],
    "Health & Wellness": ["Multivitamin Tablets","Protein Powder","Hand Sanitizer","Face Mask Pack"]
}

DIRTY_TEXT_VARIANTS = lambda s: random.choice([s.upper(), s.lower(), f" {s} ", s.replace("a", "@"), s + "  "])


def rand_date(start=START_DATE, end=END_DATE):
    return start + timedelta(days=random.randint(0, (end - start).days))


def maybe_blank(value, prob=0.05):
    return "" if random.random() < prob else value


def dirty_email(name):
    base = name.lower().replace(" ", ".")
    domain = random.choice(["gmail.com", "yahoo.com", "outlook.com", "rediffmail.com", "hotmail.com"])
    email = f"{base}{random.randint(1,999)}@{domain}"
    r = random.random()
    if r < 0.05:
        email = email.replace("@", "")
    elif r < 0.09:
        email = email.replace(".com", "")
    return email


def dirty_phone():
    num = "".join([str(random.randint(0, 9)) for _ in range(10)])
    num = random.choice(["9", "8", "7"]) + num[1:]
    r = random.random()
    if r < 0.04:
        num = num[:-random.randint(1, 3)]
    elif r < 0.08:
        num = "+91-" + num
    return num


def indian_name():
    return f"{random.choice(INDIAN_FIRST_NAMES)} {random.choice(INDIAN_LAST_NAMES)}"


def company_name():
    return f"{random.choice(COMPANY_WORDS1)} {random.choice(COMPANY_WORDS2)} {random.choice(COMPANY_SUFFIX)}"


def write_csv(filename, header, rows):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"Written {len(rows):>7} rows -> {filename}")


# -------------------------------------------------------------------
# 1. DIM_CATEGORIES (Master)
# -------------------------------------------------------------------
categories = [(i + 1, name) for i, name in enumerate(CATEGORY_NAMES)]
category_ids = [c[0] for c in categories]
write_csv("dim_categories.csv", ["category_id", "category_name"], categories)

# -------------------------------------------------------------------
# 2. DIM_STORES (Master, ~35)
# -------------------------------------------------------------------
NUM_STORES = 35
stores = []
store_ids = list(range(1, NUM_STORES + 1))
for sid in store_ids:
    city = random.choice(INDIAN_CITIES)
    state = STATES_BY_CITY[city]
    store_type = random.choice(STORE_TYPES)
    opening_date = rand_date(datetime(2015, 1, 1), datetime(2022, 12, 31))
    manager = indian_name()
    store_name = f"{city} {store_type} Store {sid}"

    r = random.random()
    if r < 0.04:
        city = DIRTY_TEXT_VARIANTS(city)
    if r < 0.03:
        opening_date_str = ""
    else:
        opening_date_str = opening_date.strftime("%Y-%m-%d")

    stores.append([sid, store_name, city, state, store_type, opening_date_str, manager])

write_csv("dim_stores.csv",
          ["store_id", "store_name", "city", "state", "store_type", "opening_date", "manager_name"],
          stores)

# -------------------------------------------------------------------
# 3. DIM_SUPPLIERS (Master, ~45)
# -------------------------------------------------------------------
NUM_SUPPLIERS = 45
suppliers = []
supplier_ids = list(range(1, NUM_SUPPLIERS + 1))
for spid in supplier_ids:
    name = company_name()
    city = random.choice(INDIAN_CITIES)
    contact_name = indian_name()
    email = dirty_email(contact_name)
    phone = dirty_phone()
    rating = round(random.uniform(1.0, 5.0), 1)

    r = random.random()
    if r < 0.03:
        rating = round(random.uniform(6.0, 10.0), 1)  # invalid outlier rating
    if r < 0.03:
        phone = ""

    suppliers.append([spid, name, city, contact_name, email, phone, rating])

write_csv("dim_suppliers.csv",
          ["supplier_id", "supplier_name", "city", "contact_name", "contact_email", "contact_phone", "rating"],
          suppliers)

# -------------------------------------------------------------------
# 4. DIM_PRODUCTS (Master, ~360)
# -------------------------------------------------------------------
NUM_PRODUCTS = 360
products = []
product_ids = list(range(1, NUM_PRODUCTS + 1))
for pid in product_ids:
    category_id = random.choice(category_ids)
    category_name = CATEGORY_NAMES[category_id - 1]
    noun = random.choice(PRODUCT_NOUN_BY_CAT[category_name])
    adj = random.choice(PRODUCT_ADJ)
    product_name = f"{adj} {noun}"
    supplier_id = random.choice(supplier_ids)
    cost_price = round(random.uniform(20, 15000), 2)
    margin = random.uniform(1.15, 1.8)
    unit_price = round(cost_price * margin, 2)

    r = random.random()
    fk_supplier = supplier_id
    if r < 0.02:
        fk_supplier = 999  # broken FK
    if r < 0.03:
        unit_price = round(cost_price * random.uniform(0.5, 0.9), 2)  # invalid: sells below cost
    if r < 0.03:
        cost_price = -cost_price  # invalid negative

    products.append([
        pid, product_name, category_id, fk_supplier,
        maybe_blank(cost_price, 0.03), unit_price
    ])

write_csv("dim_products.csv",
          ["product_id", "product_name", "category_id", "supplier_id", "cost_price_inr", "unit_price_inr"],
          products)

# -------------------------------------------------------------------
# 5. DIM_CUSTOMERS (Medium, ~6000)
# -------------------------------------------------------------------
NUM_CUSTOMERS = 6000
customers = []
customer_ids = list(range(1, NUM_CUSTOMERS + 1))
for cid in customer_ids:
    name = indian_name()
    email = dirty_email(name)
    phone = dirty_phone()
    city = random.choice(INDIAN_CITIES)
    gender = random.choice(GENDERS)
    registration_date = rand_date(datetime(2019, 1, 1), END_DATE)
    segment = random.choice(CUSTOMER_SEGMENTS)

    r = random.random()
    if r < 0.03:
        name = ""
    if r < 0.03:
        city = DIRTY_TEXT_VARIANTS(city)
    if r < 0.02:
        customers.append(customers[-1] if customers else [
            cid, name, email, phone, city, gender, registration_date.strftime("%Y-%m-%d"), segment
        ])  # duplicate row

    customers.append([
        cid, name, email, phone, city, gender,
        registration_date.strftime("%Y-%m-%d"), segment
    ])

write_csv("dim_customers.csv",
          ["customer_id", "customer_name", "email", "phone", "city", "gender",
           "registration_date", "customer_segment"],
          customers)

# -------------------------------------------------------------------
# 6. FACT_INVENTORY (Medium/Fact, ~9000) - product x store current stock snapshot
# -------------------------------------------------------------------
NUM_INVENTORY = 9000
inventory_rows = []
for i in range(1, NUM_INVENTORY + 1):
    product_id = random.choice(product_ids)
    store_id = random.choice(store_ids)
    stock_quantity = random.randint(0, 1000)
    reorder_level = random.randint(20, 150)
    last_restock_date = rand_date()

    r = random.random()
    fk_product = product_id
    fk_store = store_id
    if r < 0.02:
        fk_product = 9999  # broken FK
    if r < 0.02:
        fk_store = 999  # broken FK
    if r < 0.04:
        stock_quantity = -random.randint(1, 50)  # invalid negative stock

    inventory_rows.append([
        i, fk_product, fk_store, maybe_blank(stock_quantity, 0.03), reorder_level,
        last_restock_date.strftime("%Y-%m-%d")
    ])

write_csv("fact_inventory.csv",
          ["inventory_id", "product_id", "store_id", "stock_quantity", "reorder_level", "last_restock_date"],
          inventory_rows)

# -------------------------------------------------------------------
# 7. FACT_SALES_ORDERS (Fact, ~30000) - order header
# -------------------------------------------------------------------
NUM_ORDERS = 30000
order_rows = []
order_ids = list(range(1, NUM_ORDERS + 1))
for oid in order_ids:
    customer_id = random.choice(customer_ids)
    store_id = random.choice(store_ids)
    order_date = rand_date()
    payment_method = random.choice(PAYMENT_METHODS)
    status = random.choices(ORDER_STATUS, weights=[0.82, 0.06, 0.07, 0.05])[0]
    discount_pct = round(random.choice([0, 0, 0, 5, 10, 15, 20, 25]), 1)
    total_amount = round(random.uniform(150, 25000), 2)

    r = random.random()
    fk_customer = customer_id
    fk_store = store_id
    if r < 0.02:
        fk_customer = 99999  # broken FK
    if r < 0.02:
        fk_store = 999  # broken FK
    if r < 0.03:
        total_amount = -total_amount  # invalid negative (refund glitch)
    if r < 0.03:
        discount_pct = random.randint(80, 150)  # invalid outlier discount

    order_rows.append([
        oid, fk_customer, fk_store, order_date.strftime("%Y-%m-%d"),
        payment_method, status, discount_pct, maybe_blank(total_amount, 0.03)
    ])

# duplicate ~1%
dupe_count = int(NUM_ORDERS * 0.01)
for _ in range(dupe_count):
    order_rows.append(random.choice(order_rows))

write_csv("fact_sales_orders.csv",
          ["order_id", "customer_id", "store_id", "order_date", "payment_method",
           "order_status", "discount_pct", "total_amount_inr"],
          order_rows)

# -------------------------------------------------------------------
# 8. FACT_SALES_ORDER_ITEMS (Fact, ~48000) - line items
# -------------------------------------------------------------------
NUM_ITEMS = 48000
item_rows = []
for i in range(1, NUM_ITEMS + 1):
    order_id = random.choice(order_ids)
    product_id = random.choice(product_ids)
    quantity = random.randint(1, 10)
    unit_price = round(random.uniform(20, 15000), 2)
    discount_amount = round(unit_price * quantity * random.uniform(0, 0.3), 2)
    line_total = round((unit_price * quantity) - discount_amount, 2)

    r = random.random()
    fk_order = order_id
    fk_product = product_id
    if r < 0.02:
        fk_order = 999999  # broken FK
    if r < 0.02:
        fk_product = 9999  # broken FK
    if r < 0.03:
        quantity = -quantity  # invalid negative quantity
    if r < 0.03:
        line_total = round(line_total * random.uniform(3, 6), 2)  # outlier

    item_rows.append([
        i, fk_order, fk_product, quantity, unit_price,
        maybe_blank(discount_amount, 0.03), line_total
    ])

write_csv("fact_sales_order_items.csv",
          ["order_item_id", "order_id", "product_id", "quantity", "unit_price_inr",
           "discount_amount_inr", "line_total_inr"],
          item_rows)

# -------------------------------------------------------------------
# 9. FACT_INVENTORY_MOVEMENT (Fact, ~26000) - stock IN/OUT log
# -------------------------------------------------------------------
NUM_MOVEMENTS = 26000
movement_rows = []
for i in range(1, NUM_MOVEMENTS + 1):
    product_id = random.choice(product_ids)
    store_id = random.choice(store_ids)
    movement_type = random.choices(MOVEMENT_TYPES, weights=[0.45, 0.55])[0]
    quantity = random.randint(1, 500)
    movement_date = rand_date()
    reference_order_id = random.choice(order_ids) if movement_type == "OUT" else ""

    r = random.random()
    fk_product = product_id
    fk_store = store_id
    if r < 0.02:
        fk_product = 8888  # broken FK
    if r < 0.02:
        fk_store = 888  # broken FK
    if r < 0.03:
        quantity = 0  # invalid zero movement
    if r < 0.02 and movement_type == "OUT":
        reference_order_id = 888888  # broken FK to order

    movement_rows.append([
        i, fk_product, fk_store, movement_type, quantity,
        movement_date.strftime("%Y-%m-%d"), reference_order_id
    ])

write_csv("fact_inventory_movement.csv",
          ["movement_id", "product_id", "store_id", "movement_type", "quantity",
           "movement_date", "reference_order_id"],
          movement_rows)

print("\nAll datasets generated successfully in the 'output' folder.")
