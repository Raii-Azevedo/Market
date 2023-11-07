from typing import List, Dict
from time import sleep

from models.product import Product
from utils.helper import format_float_to_str_currency


products: List[Product] = []
shopping_cart = List[Dict[Product, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    pass

def register_product() -> None:
    pass

def list_products() -> None:
    pass

def buy_products() -> None:
    pass

def vizualize_cart() -> None:
    pass

def close_order() -> None:
    pass

def take_product_for_code(code: int) -> Product:
    pass

if __name__ == '__main__':
    main()