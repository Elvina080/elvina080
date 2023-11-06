
from selenium import webdriver

from utilities.Item_class import Item


class Cart:

        '''Класс Карзины'''
        def __init__(self, driver: webdriver.Chrome):
                self.cart = []

        # Добавление товара в карзину
        def add_to_cart(self, item : Item):
                if not isinstance(item, Item):
                        raise ValueError
                self.cart.append(item)

        # Магический метод для сравнения карзин
        def __eq__(self, other):
                if not isinstance(other, Cart):
                        raise ValueError
                first_cart = sorted(self.cart, key=lambda x: x.name_text)
                second_cart = sorted(other.cart, key=lambda x: x.name_text)
                return first_cart == second_cart
        
        # Магический метод len(cart) будет возвращать кол-во товаров в карзине
        def __len__(self):
                return len(self.cart)
        