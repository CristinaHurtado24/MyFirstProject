import requests
from Food import Food
from Drinks import Drinks
from Warehouse import Warehouse
from Modulo2 import save_data
from Modulo2 import read_data

def samandeli_api():
    
    url = 'https://saman-delivery-api.vercel.app/v1/api'

    response = requests.request('GET', url).json()
    return response

def create_warehouse(response, warehouses, codes_wh, codes_products_list):
    """[Crea objetos almacen]

    Args:
        response ([json]): [informacion de api]
        warehouses ([array]): [lista vacia de objetos almacen]
        codes_wh ([array]): [lista de codigos de almacen]
        codes_products_list ([array]): [lista de codigos producto]

    Returns:
        [array]: [lista objetos almacen]
    """

    
    for x in range(len(warehouses)):               
        print(warehouses[x])
        if not warehouses[x].code_wh in codes_wh:
            codes_wh.append(warehouses[x].code_wh)
            print(warehouses[x].code_wh)

    for wh_code in response: 
        products_l1 = []
        diagram = warehouse_diagram_generator(wh_code, response)
        code = wh_code
        products1 = response[code]['products']
        products_l1 = prods_wh(products1, products_l1, codes_wh)
        wh1_size = response[code]['warehouse']
    
        new_wh = Warehouse(code, products_l1, wh1_size, diagram)
        if not new_wh.code_wh in codes_wh:         
            warehouses.append(new_wh)
        else:
            del(new_wh)

    return warehouses

def warehouse_diagram_generator(wh_code, response):
    """[Genera el diagrama del almacen]

    Args:
        wh_code ([string]): [Codigo del almacen]
        response ([json]): [Dado por la API]

    Returns:
        [type]: [description]
    """
    diagram = {}
    
    n = response[wh_code]['warehouse'][0]  # NUMERO DE PASILLOS
    m = response[wh_code]['warehouse'][1]  # NUMERO DE ESPACIOS

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    count_corridor = 1
    count_letter = 0

    for i in range(len(response[wh_code]['products'])):
        if response[wh_code]['products'][i]['quantity'] > 0:
            while count_corridor <=n:
                spaces = {}
                while count_letter <=(m-1):
                    if i not in range(len(response[wh_code]['products'])):
                        spaces[f'{letters[count_letter]}'] = ['Available', 'No product']
                    else: 
                        spaces[f'{letters[count_letter]}'] = ['Busy', (response[wh_code]['products'][i]['code']).upper()]
                    count_letter+=1    
                    i +=1
                
                count_letter=0
                diagram[count_corridor]= spaces
                count_corridor+=1
    
    return diagram

                        
def prods_wh(products, products_list, codes_products_list):
    """[Convierte los productos dados por la API en objetos Products]

    Args:
        products ([Array]): [Lista de diccionarios dada por la API]
        products_list ([Array]): [Lista vacia]

    Returns:
        [Array]: [Lista actualizada con objetos Products]
    """
    
    for s in products_list:                    
        codes_products_list.append(products_list[s].code_prod)
    
    for i in range(len(products)):
        code = products[i]['code']
        name = products[i]['name']
        price = products[i]['price']
        quantity = products[i]['quantity']
        description = products[i]['description']
        image = products[i]['image']
        type_prod = products[i]['type']
        if type_prod == 'c':
            type_prod = 'Food'
            portion = products[i]['portion']

            new_product = Food(code.upper(), name, price, quantity, type_prod, portion, description, image)
            if not new_product.code_prod in codes_products_list:   
                products_list.append(new_product)
            else:
                del(new_product)

        else:
            type_prod = 'Drink'
            alcoholic = products[i]['alcoholic']
            new_product = Drinks(code.upper(), name, price, quantity, type_prod, alcoholic, description, image)
            if not new_product.code_prod in codes_products_list:    
                products_list.append(new_product)
            else:
                del(new_product)
    
    return products_list
        

def modulo1(warehouses, codes_products_list, codes_wh):
    response = samandeli_api()
    warehouses = create_warehouse(response, warehouses, codes_products_list, codes_wh)
    save_data('info_warehouses.txt', warehouses)

    #return warehouses

