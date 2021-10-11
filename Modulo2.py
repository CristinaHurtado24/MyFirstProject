"""MODULO DE GESTION DE PRODUCTOS
    """

from Products import Products
from Food import Food
from Drinks import Drinks
from Promotions import Promotions
from Functions import *
import webbrowser
import pickle

def save_data(file_name, list_name):
    """[guarda datos en el archivo .txt]

    Args:
        file_name ([string]): [archivo .txt]
        list_name ([array]): [lista de objetos]
    """
    archive = open(file_name, 'wb+')
    pickle.dump(list_name, archive)
    archive.close()
    del archive
    

def read_data(file_name):
    """[lee los datos guardados en el archivo .txt]

    Args:
        file_name ([string]): [archivo .txt]

    Returns:
        [array]: [lista de objetos]
    """
    
    archive = open(file_name, 'rb+')
    object_list = pickle.load(archive)
    archive.close()
    del archive
    return object_list
    

def show_product(products_list, warehouses):
    """[Funcion que muestra el producto ingresado por codigo]

    Args:
        products_list ([array]): [lista productos]
        warehouses ([array]): [lista de objetos almacen]
    """
    for x in range(len(warehouses)):
        for i in range(len((warehouses[x]).products)):
            print('\n')
            print('Product code: ',(((warehouses[x]).products)[i]).code_prod)
            print("Product's name: ",(((warehouses[x]).products)[i]).name)

    code_prod = (input('Enter the code of the product: ')).upper() 
    show_prod_info(products_list, code_prod, warehouses)


def create_new_product(products_list, warehouses):
    """[Permite crear un nuevo producto]

    Args:
        products_list ([Array]): [Lista de productos]

    Returns:
        [Array]: [Lista de productos actualizada]
    """
    print('\n')
    code_prod = verify_code_gen(products_list, warehouses)
    print(f"New product's code: {code_prod}")
    print('To create a new product please enter this requirements:')
    name = (input("Enter the new product's name: ")).title()
    _price = float(new_price())
    amount = int(new_quantity())
    image = input('Enter the URL of the picture you want to show along with your product: ')
    while (not 'https://www.' in image) and (not image[-4:]=='.jpg'):
        image = input('Enter the URL of the picture you want to show along with your product: ')
    description = (input("Please enter the product's description: ")).capitalize()

    print('\nSelect the type that matches the new product:\n1. Food\n2. Drink\n')
    prod_t = selection(3)

    if prod_t == 1:               # PRODUCTO TIPO COMIDA
        prod_type = 'Food'
        portion = input('Enter the portion of the new food (1, 2, 3... persons): ')
        while True:
            if (not portion.isnumeric()) or (int(portion) not in range(1, 31)):
                portion = input('Enter a valid portion: ')
            else:
                break
        new_product = Food(code_prod, name, _price, amount, prod_type, portion, description, image)
        locate_pro_diag(new_product, warehouses)
        

    else:                           # PRODUCTO TIPO BEBIDA
        prod_type = 'Drink'
        alcohol = (input('Enter (T) if it is an alcoholic drink, if not enter (F): ')).upper()
        while True:
            if (not alcohol.isalpha()) and (not alcohol == 'T') and (not alcohol == 'F'):
                alcohol = (input('Enter (T) if it is an alcoholic drink, if not enter (F): ')).upper()
            else:
                break

        if alcohol == 'T':
            alcoholic = 'True'
        else:
            alcoholic = 'False'

        new_product = Drinks(code_prod, name, _price, amount, prod_type, alcoholic, description, image)
        locate_pro_diag(new_product, warehouses)
    
    return warehouses


def update_product(products_list, warehouses):
    """[Permite actualizar la informacion de un producto]

    Args:
        products_list ([Array]): [Lista de productos]
    """

    for x in range(len(warehouses)):
        for i in range(len((warehouses[x]).products)):
            print('\n')
            (((warehouses[x]).products)[i]).show_product()

    print('\n')
    print(f'To update a product information please do the following: ')
    cont = '0'
    code_prod = (input('Please enter the code of the product you want to edit: ')).upper()
    for s in range(len(warehouses)):
        for x in range(len((warehouses[s]).products)):

            #ACTUALIZAR PRODUCTO TIPO COMIDA
            if (code_prod == ((((warehouses[s]).products)[x]).code_prod)) and (((((warehouses[s]).products)[x]).prod_type) == 'Food'):
                while cont == '0':
                    print(f'\n1. Change name\n2. Change Price\n3. Change product units\n4. Change description\n5. Change portion\n6. Change image\n7. Change Location')
                    option = selection(9)
                    if option == 1:
                        new_name = input("Enter the product's new name: ")
                        ((warehouses[s]).products)[x].name = new_name
                    elif option == 2:
                        new__price = new_price()
                        ((warehouses[s]).products)[x].price = new__price
                    elif option == 3:
                        n_quantity = new_quantity()
                        ((warehouses[s]).products)[x].amount = n_quantity
                    elif option == 4:
                        new_desc = input('Enter the new description: ')
                        ((warehouses[s]).products)[x].description = new_desc
                    elif option == 5:
                        new_portion = input('Enter the new portion of the product: ')
                        while True:
                            if (not new_portion.isnumeric()) or (int(new_portion) not in range(1, 31)):
                                new_portion = input('Enter a valid portion: ')
                            else:
                                break
                        ((warehouses[s]).products)[x].portion = new_portion
                    elif option == 6:

                        new_image = input('Enter the URL of the picture you want to show along with your product: ')
                        while (not 'https://www.' in new_image) and (not new_image[-4:] == '.jpg'):
                            new_image = input('Enter the URL of the picture you want to show along with your product: ')
                        ((warehouses[s]).products)[x].image = new_image

                    elif option == 7:
                        get_prod_location(warehouses, code_prod)
                    else:
                        break
                    cont = input('To upgrade another aspect of this product enter 0, if not enter another number: ')
                    save_data('info_warehouses.txt', warehouses)
                break

                #ACTUALIZAR PRODUCTO TIPO BEBIDA
            elif (code_prod == ((((warehouses[s]).products)[x]).code_prod)) and (((((warehouses[s]).products)[x]).prod_type) == 'Drink'):
                while cont == '0':
                    print(f'\n1. Change name\n2. Change Price\n3. Change product units\n4. Change description\n5. Change alcoholic grade\n6. Change image\n7. Change location')
                    option = selection(9)
                    if option == 1:
                        new_name = input("Enter the product's new name: ")
                        ((warehouses[s]).products)[x].name = new_name
                    elif option == 2:
                        new__price = new_price()
                        ((warehouses[s]).products)[x].price = new__price
                    elif option == 3:
                        n_quantity = new_quantity()
                        ((warehouses[s]).products)[x].amount = n_quantity
                    elif option == 4:
                        new_desc = input('Enter the new description: ')
                        ((warehouses[s]).products)[x].description = new_desc
                    elif option == 5:
                        alcohol = (input('Enter (T) if it is an alcoholic drink, if not enter (F): ')).upper()
                        while True:
                            if (not alcohol.isalpha()) and (not alcohol == 'T') and (not alcohol == 'F'):
                                alcohol = (input('Enter (T) if it is an alcoholic drink, if not enter (F): ')).upper()
                            else:
                                break
                        if alcohol == 'T':
                            alcoholic = 'True'
                        else:
                            alcoholic = 'False'
                        ((warehouses[s]).products)[x].alcoholic = alcoholic
    
                    elif option == 6:
                        new_image = input('Enter the URL of the picture you want to show along with your product: ')
                        while (not 'https://www.' in new_image) and (not new_image[-4:] == '.jpg'):
                            new_image = input('Enter the URL of the picture you want to show along with your product: ')
                            
                        ((warehouses[s]).products)[x].image = new_image
    
                    elif option==7:
                        get_prod_location(warehouses, code_prod)
                    else:
                        break
                    cont = input('To upgrade another aspect of this product enter 0, if not enter another number: ')
                    save_data('info_warehouses.txt', warehouses)
                break
    

def delete_product(products_list, warehouses):
    """[Permite eliminar un producto de la lista]

    Args:
        products_list ([Array]): [Lista de productos]

    Raises:
        Exception: [ValueError]

    Returns:
        [Array]: [Lista de productos actualizada]
    """

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
 
    for x in range(len(warehouses)):
        for i in range(len((warehouses[x]).products)):
            print('\n')
            (((warehouses[x]).products)[i]).show_product()

    code_prod = (input('\nEnter the code of the product: ')).upper()
    for x in range(len(warehouses)):
        for i in range(len((warehouses[x]).products)):
            if code_prod == (((warehouses[x]).products)[i].code_prod):
                show_prod_info(products_list, code_prod, warehouses)  
                print(f'\nAre you sure you want to delete this product? ')
                decision = (input('To delete the product please enter (D), otherwise enter (N):')).upper()
                while True:
                    if (not decision == 'D') and (not decision == 'N'):
                        decision = (input('To delete the product please enter (D), otherwise enter (N):')).upper()
                    else:
                        break
                if decision == 'D':
                    del_prod_yes(products_list, warehouses, code_prod)
                else:
                    print('Cancelled!!')
                    break

def del_prod_yes(products_list, warehouses, code_prod):
    """[Elimina el producto]

    Args:
        products_list ([array]): [lista de objetos producto]
        warehouses ([array]): [lista de objetos almacen]
        code_prod ([string]): [codigo del producto a eliminar]
    """

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for u in range(len(warehouses)):
        for a in range(len((warehouses[u]).products)):
            if code_prod == (((warehouses[u]).products)[a].code_prod):
                for s in range(len((warehouses[u]).wh_diagram)):  # Num pasillo
                    for w in range(0, ((warehouses[u]).wh_size)[1]):  # Num espacio
                        if ((warehouses[u]).wh_diagram)[s+1][letters[w]][1] == code_prod:
                            ((warehouses[u]).wh_diagram)[s+1][letters[w]] = ['Available', 'No Product']
                            del(((warehouses[u]).products)[a])
                            save_data('info_warehouses.txt', warehouses)
                            print('Product deleted!!')


def promotions(promotions_list):
    """[Permite crear, mostrar y eliminar promociones del sistema]

    Args:
        promotions_list ([Array]): [Lista de promociones]

    Returns:
        [Array]: [Lista de promociones actualizada]
    """
    while True:
        print('\n1. Create promotion\n2. Show promotions\n3. Delete promotion\n4. Exit')
        prom = selection(5)

        if prom == 1:            #CREAR PROMOCION
            prom_code = (input("Please, enter the new promotion's code: ")).upper()
            promotions_list = read_data('promotions.txt')
            prom_code = verify_promo_code(promotions_list, prom_code)
            percent = percentage()
            new_promotion = Promotions(prom_code, percent)
            promotions_list.append(new_promotion)
            save_data('promotions.txt', promotions_list)

        elif prom == 2:         #MOSTRAR PROMOCIONES
            promotions_list = read_data('promotions.txt')
            if len(promotions_list)==0:
                print('Sorry, the data base does not contain any promotion')
            else:
                print('\n')
                for i, promo in enumerate(promotions_list):
                    print('Promotion number---', i+1, '-----')
                    print(promo.show_promotion())
                    print('\n')

        elif prom == 3:         #ELIMINAR PROMOCIONES
            print('\n')
            promotions_list = read_data('promotions.txt')
            pr_code =input('Enter the code of the promotion you want to delete: ')
            show_promo_info(promotions_list, pr_code)
            print(f'Are you sure you want to delete this promotion? ')
            decision = (input('To delete the promotion please enter (D), otherwise enter (N):')).upper()
            while True:
                if (not decision == 'D') and (not decision == 'N'):
                    decision = (input('To delete the promotion please enter (D), otherwise enter (N):')).upper()
                else:
                    break
            if decision == 'D':
                for x in range(len(promotions_list)):
                    if pr_code == promotions_list[x].code_prom:
                        save_data('promotions.txt', promotions_list)
                        del(promotions_list[x])
                print('Promotion deleted!!')
            else:
                print('Cancelled!!')
                break
        else:
            break
    return promotions_list


def promotions_1(promotions_list):
    """[Permite crear, mostrar y eliminar promociones del sistema]

    Args:
        promotions_list ([Array]): [Lista de promociones]

    Returns:
        [Array]: [Lista de promociones actualizada]
    """
    while True:
        print('\n1. Create promotion\n2. Show promotions\n3. Delete promotion\n4. Exit')
        prom = selection(5)

        if prom == 1:  # CREAR PROMOCION
            prom_code = (input("Please, enter the new promotion's code: ")).upper()
            prom_code = verify_promo_code(promotions_list, prom_code)
            percent = percentage()
            new_promotion = Promotions(prom_code, percent)
            promotions_list.append(new_promotion)
            save_data('promotions.txt', promotions_list)

        elif prom == 2:  # MOSTRAR PROMOCIONES
            if len(promotions_list) == 0:
                print('Sorry, the data base does not contain any promotion')
            else:
                print('\n')
                for i, promo in enumerate(promotions_list):
                    print('Promotion number---', i+1, '-----')
                    print(promo.show_promotion())
                    print('\n')

        elif prom == 3:  # ELIMINAR PROMOCIONES
            print('\n')
            pr_code = input(
                'Enter the code of the promotion you want to delete: ')
            show_promo_info(promotions_list, pr_code)
            print(f'Are you sure you want to delete this promotion? ')
            decision = (
                input('To delete the promotion please enter (D), otherwise enter (N):')).upper()
            while True:
                if (not decision == 'D') and (not decision == 'N'):
                    decision = (
                        input('To delete the promotion please enter (D), otherwise enter (N):')).upper()
                else:
                    break
            if decision == 'D':
                for x in range(len(promotions_list)):
                    if pr_code == promotions_list[x].code_prom:
                        save_data('promotions.txt', promotions_list)
                        del(promotions_list[x])
                print('Promotion deleted!!')
            else:
                print('Cancelled!!')
                break
        else:
            break
    return promotions_list

def modulo2_productos(products_list, warehouses):
    """[Main page del Modulo de Gestion de productos]
    """
    while True:
        print('\n')
        print('1. Show product\n2. Create a new product\n3. Update product information\n4. Delete product\n5. Exit ')
        select = selection(6)

        if select == 1:  # MOSTRAR PRODUCTOS
            warehouses = read_data('info_warehouses.txt')
            show_product(products_list, warehouses)
    
        elif select == 2:  # CREAR NUEVO PRODUCTO
            
            warehouses = read_data('info_warehouses.txt')
            warehouses = create_new_product(products_list, warehouses)
            save_data('info_warehouses.txt', warehouses)

        elif select == 3:  # ACTUALIZAR PRODUCTO
            warehouses = read_data('info_warehouses.txt')
            update_product(products_list, warehouses)
            save_data('info_warehouses.txt', warehouses)

        elif select == 4:  # ELIMINAR PRODUCTO
            warehouses = read_data('info_warehouses.txt')
            delete_product(products_list, warehouses)
            save_data('info_warehouses.txt', warehouses)
        else:
            break
    

def modulo2_promociones(promotions_list):
    """[Se ejecuta al usuario ingresar al programa por segunda vez]

    Args:
        promotions_list ([array]): [lista de objetos promociones]

    Returns:
        [array]: [lista de objetos promociones]
    """
    promotions_list = promotions(promotions_list)

    return promotions_list


def modulo2_promociones1(promotions_list):
    """[Se ejecuta al usuario ingresar al programa por primera vez]

    Args:
        promotions_list ([array]): [lista de objetos promociones]

    Returns:
        [array]: [lista de objetos promociones]
    """
    promotions_list = promotions_1(promotions_list)

    return promotions_list

def delivery_fee(deli_fee):
    """[Se ejecuta al usuario ingresar al programa por segunda vez]

    Args:
        deli_fee ([float]): [Fee del delivery]

    Returns:
        [float]: [Fee del delivery]
    """
    delivery_fee = read_data('delivery.txt')
    while True:
        print(
            "\n1. Update delivery's fee\n2. Show Delivery's fee\n3. Exit")
        option = selection(4)
        if option == 1:
            fee = input("Please enter the new deliver's fee: ")
            while (not fee.isnumeric()) and (not float(fee) > 0.0):
                fee = input("Please enter a valid value: ")
            delivery_fee = float(fee)
            save_data('delivery.txt', delivery_fee)
            print(f"The delivery's fee has been updated to ${delivery_fee}")
        elif option == 2:
            print(f"\nThe actual delivery's fee is ${delivery_fee}")
        else:
            break
    return delivery_fee


def delivery_fee1(deli_fee):
    """[Se ejecuta al usuario ingresar al programa por primera vez]

    Args:
        deli_fee ([float]): [Fee del delivery]

    Returns:
        [float]: [Fee del delivery]
    """
    delivery_fee = deli_fee
    while True:
        print(
            "\n1. Update delivery's fee\n2. Show Delivery's fee\n3. Exit")
        option = selection(4)
        if option == 1:
            fee = input("Please enter the new deliver's fee: ")
            while (not fee.isnumeric()) and (not float(fee) > 0.0):
                fee = input("Please enter a valid value: ")
            delivery_fee = float(fee)
            save_data('delivery.txt', delivery_fee)
            print(f"The delivery's fee has been updated to ${delivery_fee}")
        elif option == 2:
            print(f"\nThe actual delivery's fee is ${delivery_fee}")
        else:
            break
    return delivery_fee

def change_order_status(sales):
    while True:
        print('\nHello. What would you like to do?\n1. Show orders\n2. Change order status\n3. Exit')
        select = selection(4)

        if select==1:               ##MOSTRAR ORDENES
            if len(sales) ==0:
                print('There are no orders')
                break
            else:
                for i, sale in enumerate(sales):
                    print('\n')
                    print('Order----',i+1,'----')
                    sale.show_invoice()

        elif select==2:             ##CAMBIAR STATUS DE LAS ORDENES
            if len(sales) ==0:
                print('There are no orders')
                break

            else:
                for i, sale in enumerate(sales):
                    print('\n')
                    print('Order----',i+1,'----')
                    sale.show_invoice()
                
                option=input('\nEnter the number of the order you want to change the status: ')
                while (not option.isnumeric()) and (not int(option)>=1):
                    option = input('Enter the number of the order you want to change the status: ')

                for i, sale in enumerate(sales):
                    if int(option)-1 ==i:
                        print(sale.order_status)
                        change= (input('\nEnter Y(yes) if you want to change the order status, if not enter N(no): ')).upper()
                        while (not change.isalpha()) and (not change =='Y') and (not change=='N'):
                            change = (input('Enter Y(yes) if you want to change the order status, if not enter N(no): ')).upper()
                        if change=='Y':
                            sale.order_status ='Delivered'
                            save_data('sales.txt', sales)
                            print('Order status updated to "Delivered"')
                            break
                        else:
                            print('The order status will remain as it was.')
                            break
                        break


        else:
            break
