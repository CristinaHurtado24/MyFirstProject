"""[MODULO DE VENTAS]
    """

from Clients import Clients
from Sales import Sales
from Products import Products
from Functions import selection
from Functions import show_all_products
from Functions import select_prod
from Functions import show_promo_main
from Functions import delete_prod_client
from Functions import check_out
from Functions import show_prod_selected
import pickle


def save_data2(file_name, list_name):
    """[guarda datos en el archivo .txt]

    Args:
        file_name ([string]): [archivo .txt]
        list_name ([array]): [lista de objetos]
    """

    archive = open(file_name, 'wb+')
    pickle.dump(list_name, archive)
    archive.close()
    del archive


def read_data2(file_name):
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



def register_client(clients_list):
    """[Solicita la informacion pertinente para el registro del cliente]

    Args:
        clients_list ([Arraay]): [Lista de clientes]

    Returns:
        [Array]: [Lista de clientes actualizada]
    """


    name = (input('\nPlease enter your name: ')).title()
    while not ("".join(name.split(" "))).isalpha():
        name = (input('Please enter a valid name: ')).title()

    email = input('\nPlease enter your email address: ')
    while (not '@' in email) or (not '.com' in email[-4:]):
        email = input('Error. Please enter a valid email address: ')

    password = input('\nEnter your password (min 8 caracters): ')
    while (not len(password)>8):
        password = input('\nYour passwrod must have at least 8 caracters: ')

    new_client = Clients(name, email, password)
    clients_list.append(new_client)
    save_data2('clients.txt', clients_list)
    print('You are now registered!!')
    return clients_list

def log_in(clients_list, deli_fee, promotions_list, sales_, warehouses):
    """[Permite iniciar sesion la cliente y realizar su compra, se ejecuta a la segunda vez de abrir el programa]

    Args:
        clients_list ([array]): [lista de objetos cliente]
        deli_fee ([float]): [fee del delivery]
        promotions_list ([array]): [lista de objetos promocion]
        sales_ ([array]): [lista de objetos sales]
        warehouses ([array]): [lista de objetos almacen]

    Returns:
        [array]: [lista de objetos sales]
    """
    print('\n')
    products_list =[]
    e_mail = input('Please enter your email address: ')
    while (not '@' in e_mail) or (not '.com' in e_mail[-4:]):
        e_mail = input('Error. Please enter a valid email address: ')
    
    clients_list = read_data2('clients.txt')
    for x in range(len(clients_list)):
        if e_mail == clients_list[x].email:
            password = input('Please enter your password: ')
            if password == clients_list[x].get_password():
                prod_client_list = []
                password = clients_list[x].get_password()
                name = clients_list[x].name
                email = clients_list[x].email
                print(f'Welcome back {clients_list[x].name}')
                while True:
                    print('\nWhat would you like to do next?\n1. Add products to your car\n2. Delete products from your car\n3. Check-Out section\n4. Show order status\n5. Exit')
                    option = selection(6)

                    if option==1:     #AGREGAR PRODUCTOS AL CARRITO DE COMPRAS
                    
                        print('\nYou will find our products right bellow:\n')
                        show_all_products(warehouses, products_list)
                        print('\n')
                        products_selected = select_prod(warehouses, prod_client_list, products_list)
                        print('\nProducts in your car:\n')
                        show_prod_selected(products_selected)

                    elif option==2:   #ELIMINAR PRODUCTOS DEL CARRITO DE COMPRAS
                        if len(prod_client_list)==0:     
                            print('First you have to add some products to your car!')
                        else:
                            prod_client_list = delete_prod_client(products_selected)
                    
                    elif option==3:   #CHECK-OUT
                        if len(prod_client_list)==0:
                            print('You have to add products to your car to do a check-out.')
                        else:
                            sales_ = check_out(warehouses, prod_client_list, deli_fee, promotions_list, sales_, name, email, password)
                            save_data2('sales.txt', sales_)
                    
                    elif option==4:  #ORDER STATUS
                        sales_ = read_data2('sales.txt')
                        if len(sales_)==0:
                            print('Oops something went wrong')
                        else:
                            for x in range(len(sales_)):
                                if sales_[x].name == name:
                                    sales_[x].show_invoice()
                                else:
                                    print('Oops it seems like you do not have made an order yet...')
                    else:
                        break
            else:
                print('Oops... The value you entered is incorrect')
                break
    return sales_


def log_in1(clients_list, deli_fee, promotions_list, sales_, warehouses):
    """[Permite iniciar sesion la cliente y realizar su compra, se ejecuta a la primera vez de abrir el programa]

    Args:
        clients_list ([array]): [lista de objetos cliente]
        deli_fee ([float]): [fee del delivery]
        promotions_list ([array]): [lista de objetos promocion]
        sales_ ([array]): [lista de objetos sales]
        warehouses ([array]): [lista de objetos almacen]

    Returns:
        [array]: [lista de objetos sales]
    """
    print('\n')
    products_list = []
    e_mail = input('Please enter your email address: ')
    while (not '@' in e_mail) or (not '.com' in e_mail[-4:]):
        e_mail = input('Error. Please enter a valid email address: ')

    clients_list = read_data2('clients.txt')
    for x in range(len(clients_list)):
        if e_mail == clients_list[x].email:
            password = input('Please enter your password: ')
            if password == clients_list[x].get_password():
                prod_client_list = []
                password = clients_list[x].get_password()
                name = clients_list[x].name
                email = clients_list[x].email
                print(f'Welcome back {clients_list[x].name}')
                while True:
                    print('\nWhat would you like to do next?\n1. Add products to your car\n2. Delete products from your car\n3. Check-Out section\n4. Show order status\n5. Exit')
                    option = selection(6)

                    if option == 1:  # AGREGAR PRODUCTOS AL CARRITO DE COMPRAS

                        print('\nYou will find our products right bellow:\n')
                        show_all_products(warehouses, products_list)
                        print('\n')
                        products_selected = select_prod(warehouses, prod_client_list, products_list)
                        print('\nProducts in your car:\n')
                        show_prod_selected(products_selected)

                    elif option == 2:  # ELIMINAR PRODUCTOS DEL CARRITO DE COMPRAS
                        if len(prod_client_list) == 0:  
                            print('First you have to add some products to your car!')
                        else:
                            prod_client_list = delete_prod_client(products_selected)

                    elif option == 3:   #CHECK-OUT
                        if len(prod_client_list) == 0:
                            print('You have to add products to your car to do a check-out.')
                        else:
                            sales_ = check_out(warehouses, prod_client_list, deli_fee, promotions_list, sales_, name, email, password)
                            save_data2('sales.txt', sales_)

                    elif option == 4:   #ORDER STATUS
                        sales_ = read_data2('sales.txt')
                        if len(sales_) == 0:
                            print('Oops something went wrong')
                        else:
                            for x in range(len(sales_)):
                                if sales_[x].name == name:
                                    sales_[x].show_invoice()
                                else:
                                    print('Oops it seems like you do not have made an order yet...')
                    else:
                        break
            else:
                print('Oops... The value you entered is incorrect')
                break
    return sales_

def modulo3(clients_list, promotions_list, deli_fee, sales_, warehouses):
    """[Main del modulo 3, se ejecuta a la segunda vez de iniciar el programa]

    Args:
        clients_list ([array]): [lista de objetos cliente]
        promotions_list ([array]): [lista de objetos promocion]
        deli_fee ([float]): [fee del delivery]
        sales_ ([array]): [lista de objetos sales]
        warehouses ([array]): [lista de objetos almacen]

    Returns:
        [array]: [lista de objetos sales]
    """
    print('***WELCOME TO SAMAN-DELIVERY!!***\n')
    show_promo_main(promotions_list)
    print('Please log in or register to get started')
    while True:
        print('\n1. Register\n2. Log In\n3. Exit')
        option = selection(4)
    
        if option == 1:  # REGISTRAR CLIENTE
            clients_list = register_client(clients_list)

        elif option == 2:  # INICIAR SESION
           sales_ = log_in(clients_list, deli_fee, promotions_list, sales_, warehouses)
    
        else:
            break
    return sales_


def modulo3_1(clients_list, promotions_list, deli_fee, sales_, warehouses):
    """[Main del modulo 3, se ejecuta a la primera vez de iniciar el programa]

    Args:
        clients_list ([array]): [lista de objetos cliente]
        promotions_list ([array]): [lista de objetos promocion]
        deli_fee ([float]): [fee del delivery]
        sales_ ([array]): [lista de objetos sales]
        warehouses ([array]): [lista de objetos almacen]

    Returns:
        [array]: [lista de objetos sales]
    """
    print('***WELCOME TO SAMAN-DELIVERY!!***\n')
    show_promo_main(promotions_list)
    print('Please log in or register to get started')
    while True:
        print('\n1. Register\n2. Log In\n3. Exit')
        option = selection(4)

        if option == 1:  # REGISTRAR CLIENTE
            clients_list = register_client(clients_list)

        elif option == 2:  # INICIAR SESION
           sales_ = log_in1(clients_list, deli_fee,promotions_list, sales_, warehouses)

        else:
            break
    return sales_
