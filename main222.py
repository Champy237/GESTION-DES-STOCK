
# coding:UTF-8

import sqlite3
import datetime

conn = sqlite3.connect('gestion_stock.db')
cursor = conn.cursor()

def createPD_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        price INTEGER,
        category TEXT,
        quantity INTEGER,
        supplier INTEGER,
        FOREIGN KEY (supplier) REFERENCES suppliers(id)
                                   
    )""")


def insert_PD(product):
    cursor.execute("""
        INSERT INTO product(price,category,quantity,supplier)
        VALUES(?,?,?,?)
    """, product)
    conn.commit()


def afficher_PD():
    req = cursor.execute("SELECT * FROM product")

    product = req.fetchall() 
    
    for display in product:
        print("---------------------------------------\n")
        print("ID        : {}".format(display[0]))
        print("PRIX      : {}".format(display[1]))
        print("CATEGORIE : {}".format(display[2]))
        print("QUANTITÉ  : {}".format(display[3]))
        print("LIVREUR   : {}".format(display[4]))
        print("\n")
        print("---------------------------------------")


def check_PD(id_product):
    req = cursor.execute("SELECT * FROM product WHERE id = ? ", (id_product,))
    product = req.fetchall() 

    if product:
        print("produit retrouvé !!!")
        for display in product:
            print("---------------------------------------\n")
            print("ID        : {}".format(display[0]))
            print("PRIX      : {}".format(display[1]))
            print("CATEGORIE : {}".format(display[2]))
            print("QUANTITÉ  : {}".format(display[3]))
            print("LIVREUR   : {}".format(display[4]))
            print("\n")
            print("---------------------------------------")
    else :
        print("produit non retrouvé !!!")

def update_PD(value):
    req = "UPDATE product SET price = ?, category = ?, quantity = ?, supplier = ? WHERE id = ?"
    cursor.execute(req, value)
    conn.commit()
       
def delete_PD(id_product):
    req = "DELETE FROM product WHERE id = ?"
    cursor.execute(req,(id_product,))
    conn.commit()
    
def restock_PD(id_product, quantity):
    req = "UPDATE product SET quantity = quantity + ? WHERE id = ?"
    cursor.execute(req, (quantity, id_product))
    conn.commit()
    
def check_inventory_PD(id_product):
    req = cursor.execute("SELECT quantity FROM product WHERE id = ?",(id_product,))
    quantity = req.fetchone()
    if quantity and quantity[0] > 0:
         print("quantity : {}".format(quantity[0]))
         return True
    return False

def search_products_PD(search_term):
    req = """SELECT * FROM product 
             WHERE category LIKE ? OR
                  id LIKE ? OR
                  supplier LIKE ? """
    cursor.execute(req,(f"%{search_term}%",f"%{search_term}%",f"%{search_term}%"))
    products = cursor.fetchall()
    return products

def create_order_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        date1 DATE,
        customer_id INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customer(id)
                                  
    )""")

def create_order_item_table():
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_items(
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY (order_id) REFERENCES orders(id),
            FOREIGN KEY (product_id) REFERENCES product(id),
            PRIMARY KEY (order_id, product_id)
                                          
        )""")
def insert_order(customer_id):
    date = datetime.date.today()
    req = "INSERT INTO orders (date1,customer_id) VALUES (?,?)"
    cursor.execute(req,(date,customer_id))
    conn.commit()
    return cursor.lastrowid

def insert_order_item(order_id,product_id,quantity):
    req = "INSERT INTO order_items (order_id,product_id,quantity) VALUES (?,?,?)"
    cursor.execute(req,(order_id,product_id,quantity))
    conn.commit()

def process_order_PD(order_id):
    req = cursor.execute("SELECT product_id,quantity FROM order_items WHERE order_id = ?", (order_id,))
    products = req.fetchall()
    for product_id,quantity in products:
        req_update = "UPDATE product SET quantity = quantity - ? WHERE id = ?"
        cursor.execute(req_update,(quantity,product_id))
        conn.commit()

def cancel_order_PD(order_id):
     req = cursor.execute("SELECT product_id,quantity FROM order_items WHERE order_id = ?", (order_id,))
     products = req.fetchall()
     for product_id,quantity in products:
            req_update = "UPDATE product SET quantity = quantity + ? WHERE id = ?"
            cursor.execute(req_update,(quantity,product_id))
            conn.commit()
     req_delete = "DELETE FROM orders WHERE id = ?"
     cursor.execute(req_delete,(order_id,))
     conn.commit()

def createSU_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS suppliers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        name TEXT,
        adresse TEXT,
        telephone INTEGER                                  
    )""")


def createCU_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer(
        id INTEGER PRIMARY KEY AUTOINCREMENT,   
        name TEXT,
        adresse TEXT,
        telephone INTEGER                                 
    )""")


def createCOM_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS commande(
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        date1 DATE,
        customer_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customer(id)
        FOREIGN KEY (product_id) REFERENCES product(id)                                   
    )""")
conn.close()
