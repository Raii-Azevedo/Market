from typing import List, Dict
from time import sleep

from models.product import Product
from utils.helper import format_float_to_str_currency


products: List[Product] = []
shopping_cart: List[Dict[Product, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('== '*24)
    print('== '*10, '= Welcome =', ' =='*10)
    print('== '*10, 'Market Shop', ' =='*10)
    print('== '*24)
    
    print('\nSelect an option: ')
    print('''    \n[1] Register Product\n[2] List Products\n[3] Buy a Product\n[4] Vizualize Shop Cart\n[5] Close Order\n[6] Exit System\n''')

    option: int = int(input())

    if option == 1:
        register_product()
    elif option == 2:
        list_products()
    elif option == 3:
        buy_products()
    elif option == 4:
        vizualize_cart()
    elif option == 5:
        close_order()
    elif option == 6:
        print('\nThank you. Comeback Soon!')
        sleep(2)
        exit(0)
    else:
        print('Invalid option. Choose between [1] and [6]\n')
        sleep(2)
        menu()

def register_product() -> None:
    print('Register Product\n')

    name: str = input('Name of the product: ')
    price: float = float(input('Price of Product R$: '))

    product: Product = Product(name, price)

    products.append(product)

    print(f'The Product {product.name} was successfully registered!\n')
    sleep(2)
    menu()

def list_products() -> None:
    if len(products) > 0:
        print('List of Products\n')

        for product in products:
            print(product)
            print('----------')
            sleep(0.5)
    else:
        print('There is no products registered yet\n')
    sleep(2)
    menu()

def buy_products() -> None: # The most complex function
    if len(products) > 0:
        print('Enter the code of the product you want to add to the cart: ')
        print('---'*30)
        print('==== Available Products  ====')
        
        for product in products:
            print(product)
            print('---' *10)
            sleep(0.5)
        code: int = int(input())

        product: Product = take_product_for_code(code)

        if product: 
            if len(shopping_cart) > 0:
                on_cart: bool = False
                
                for item in shopping_cart:
                    quantity: int = item.get(product)
                    if quantity: 
                        item[product] = quantity + 1
                        print(f'The product {product.name} has {quantity + 1} units in cart')
                        on_cart = True
                        sleep(2)
                        menu()

                if not on_cart:
                    prod = {product: 1}
                    shopping_cart.append(prod)
                    print(f'The product {product.name} was successfully added to the cart!\n')
                    sleep(2)
                    menu()

            else:
                item = {product: 1}
                shopping_cart.append(item)
                print(f'The product {product.name} was successfully added to the cart\n')
                sleep(2)
                menu()

        else:
            print(f'The product with code {code} was not found\n')
            sleep(2)
            menu()

    else:
        print('There is no products to sale yet\n')
    sleep(2)
    menu()
    
def vizualize_cart() -> None:
    if len(shopping_cart) > 0:
        print('Products on Cart: ')

        for item in shopping_cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print('---'*10)
                sleep(0.5)
    
    else:
        print('There is no products on cart yet\n')
    sleep(2)
    menu()

def close_order() -> None:
    if len(shopping_cart) > 0:
        total_value: float = 0
        print('Products in the Cart')

        for item in shopping_cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print('----------')
                sleep(1)
                total_value += data[0].price * data[1]  # Mova esta linha para fora do loop interno

        print(f' Your bill is {format_float_to_str_currency(total_value)}')  # Mova esta linha para fora do loop interno
        print('\nComeback Soon')
        shopping_cart.clear()
        sleep(4)
        menu()
    else:
       print('There is no products in the cart yet\n') 
    sleep(2)
    menu()


def take_product_for_code(code: int) -> Product:
    p: Product = None

    for product in products:
        if product.code == code:
            p = product
    return p

if __name__ == '__main__':
    main()