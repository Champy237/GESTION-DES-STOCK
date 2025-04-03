#codin:utf-8

from fonction import *
from os import *


system("clear")
choix = 0

while choix != 5:
    print("\t\t\tBIENVENUE DANS LOGICIELLE DE GESTION DES STOCK")
    print("\n")
    print("1. Gestion des produit")
    print("2. Gestion des Commende")
    print("3. Gestion des Inventaire et réapprovisionnement ")
    print("4. Sortit ..........")
    choix = int(input("faite un choix  : "))

    match choix:
        case 1:
            Product.gestion_des_product(product=())
            continue
        case 2:
            Product.gestionCommandes()
            continue
        case 3:
            Product.gestionaireInventaire()
            continue
        case 4:
            print("Au revoir")
            break
        case _:
            print("mauvaise valeur")
            continue


