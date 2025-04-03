#coding:UTF-8
from sqlite import *
from os import *
from time import *


class Product:

    def __init__(self,id,price,category,quantity,supplier):
        self.id = id
        self.price = price
        self.category= category
        self.quantity = quantity
        self.supplier = supplier
        self.order_id = None
        self.customer_id = None
    
    def init():
        createPD_table()

    def update_price(price,categoriste,quantity,supplier):
        product = (price,categoriste,quantity,supplier)
        insert_PD(product)
    
    def display_PD():
        system("clear")
        print("  \t\t--------- LISTE DES PRODUIT ------------ ")
        afficher_PD()
    
    def check_outPD(id_product):
        check_PD(id_product)

    def update_product(self):
        value = (self.price, self.category, self.quantity, self.supplier, self.id)
        update_PD(value)

    def delete_product(id_product):
        delete_PD(id_product)



    def gestion_des_product(product):
            system("clear")
            choix = '0' 
            Product.init()
            Supplier.init()
            Customer.init()
            Command.init()

            while choix!='6' :

                
                print("\t\t\tBIENVENUE DANS LE MENU GESTION DES PRODUIT")
                print("1. enregistrer un produit")
                print("2. effectuer la recherche d'un produit")
                print("3. modifier les info d'un produit ")
                print("4. supprimer un produit")
                print("5. afficher la liste des produit ")
                choix = input("choix : ")

                match choix:

                    case "1":

                        price = int(input("entrer prix :"))
                        categoriste = input("entrer  votrer categorie :")
                        quantity = input("enter quantity :")
                        supplier = int(input("input supplier :"))

                        product = (price,categoriste,quantity,supplier)

                        Product.update_price(price,categoriste,quantity,supplier)

                        continue

                    case "2":

                        id_product = int(input("entrer le id du produit :"))

                        Product.check_outPD(id_product)

                        continue

                    case "3":

                        id_product = int(input("entrer le id du produit :"))


                        Product.check_outPD(id_product)

                        print(" entrer les nivelles information ")

                        price = int(input("entrer prix :"))

                        category = input("entrer  votrer categorie :")

                        quantity = input("enter quantity :")

                        supplier = int(input("input supplier :"))

                        prod = Product(id_product,price ,category,quantity,supplier)
                        prod.update_product()

                        continue

                    case "4":

                        id_product = int(input("entrer le id du produit :"))


                        Product.check_outPD(id_product)

                        Product.delete_product(id_product)
                        print("Produit supprimé.")
                        sleep(1)
                        continue


                    case "5":

                        Product.display_PD()

                        continue

                    case "6":
                        print("revenir au menue principale")

                    case _:
                        print("mauvais choix faire un autre choix")
    
    
    def check_inventory(self):
        return check_inventory_PD(self.id)
    
    def insert_order(self,product):
        self.order_id = insert_order(self.customer_id)
        for product_id, quantity in product:
            insert_order_item(self.order_id,product_id,quantity)

    def process_order(self):
        process_order_PD(self.order_id)

    def cancel_order(self):
        cancel_order_PD(self.order_id)

    def Display_order():
        affichage_commande()


    @staticmethod
    def gestionCommandes():
        system("clear")
        choix = 0
        while choix != 5:
            print("\n -----BIENVUE DANS LA GESTION DES COMMANDS ---")
            print("1. Créer une commande")
            print("2. Traiter une commande")
            print("3. Annuler une commande")
            print("4. afficher liste des commandes")
            print("5. revenir au menu principale")
            choix = input("Votre choix : ")
            
            match choix:
                case "1":
                    customer_id = int(input("Entrer l'ID du client : "))
                    products = []

                    while True:
                        product_id = int(input("Entrer l'ID du produit : "))
                        quantity = int(input("Quantité : "))
                        products.append((product_id, quantity))
                        more = input("Ajouter un autre produit ? (o/n) : ")
                        if more.lower() != 'o':
                            break
                    prod = Product(None, 0, '', 0, 0)
                    prod.customer_id = customer_id
                    prod.insert_order(products)
                    continue


                case "2":

                    order_id = int(input("Entrer l'ID de la commande à traiter : "))
                    req = cursor.execute("SELECT id FROM orders WHERE id = ?", (order_id,))
                    order = req.fetchone()

                    if order:
                        prod = Product(None, 0, '', 0, 0)
                        prod.order_id = order_id
                        prod.process_order()
                    else:
                        print("Commande non trouvée.")
                    continue

                case "3":

                    order_id = int(input("Entrer l'ID de la commande à annuler : "))
                    prod = Product(None, 0, '', 0, 0)
                    prod.order_id = order_id
                    prod.cancel_order()

                    continue
                case "4":
                    Product.Display_order()
                    continue
                case _:
                    print("Choix invalide. Veuillez réessayer.")
                    break



        
    
    def check_inventory(self):
        return check_inventory_PD(self.id)
    
    @staticmethod
    def gestionaireInventaire():

        system("clear")

        choix = "0"

        while choix != "6":
            print("\t\tBIENVENUE DANS LE MENU DE GESTION DES IVENTAIRE")
            print("1. pour la gestion des inventaire")
            choix = input("choix :")
            match choix:
                case "1":
                    order_id = int(input("Entrer l'ID du produit pour verifier l'inventaire : "))
                    prod = Product(id=order_id, price=None, category=None, quantity=None, supplier=None)
                    if prod.check_inventory():
                        print("Le produit est en stock.")
                    else:
                        print("Le produit n'est pas en stock")
                    continue









class Supplier:

    def __init__(self,id,nom,adresse,telephone):
        self.id = id
        self.nom = nom
        self.adresse = adresse
        self.telephone = telephone
    
    def init():
        createSU_table()

    
    
    

class Customer:

    def __init__(self,id,nom,adresse,telephone):
        self.id = id
        self.nom = nom
        self.adresse = adresse
        self.telephone = telephone

    def init():
        createCU_table
    

class Command:

    def __init__(self,id,date,customer,product,quantity):
        self.id = id
        self.date = date
        self.customer = customer
        self.product = product
        self.quantity = quantity

    def init():
        createCOM_table



product = ()


