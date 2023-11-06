
from selenium import webdriver
from utilities.Item_class import Item
from utilities.Cart_class import Cart
from base.Base_class import Base



class Main_page(Base):
        
        start_url = 'https://dodopizza.ru/moscow/pavlakorchagina13s1'

        def __init__(self, driver : webdriver):
                super().__init__(driver)
                self.cart = Cart(self.driver)

        # Anchor (якори)

        categoryes = {'pizza' : 'guzhy',
        'combo' : 'nfjka',
        'snack' : 'kxgls', 
        'coctail' : 'mrwqq',
        'coffe' : 'dtgyl', 
        'drink' : 'zzvck', 
        'dessert' : 'uzlth', 
        'sauce' : 'auyfy',
        'good' : 'thffj'}



        # Locators

        ## Locator constructor
        
        # Получение локатора цены
        def price_xpath(self, anchor, num):
                return f'//*[@id="{anchor}"]/article[{num}]/footer/div' 
        # Получение локатора названия товара
        def item_name_xpath(self, anchor, num):
                return f'//*[@id="{anchor}"]/article[{num}]/main/div/a'


        # Getters
        
        # Элемент цена твоара
        def get_price(self, anchor, num):
                return self.get_element(xpath=self.price_xpath(anchor, num))
        # Элемент название товара
        def get_item_name(self, anchor, num):
                return self.get_element(xpath=self.item_name_xpath(anchor, num))
        # Получене текста якоря по категории товара
        def get_category_value(self, cat_name):
                return self.categoryes.get(cat_name)

        
        # Actions

        # Открытие ссылки
        def open_page(self):
                self.driver.get(self.start_url)

        # Инициализация объекта товара
        def take_item(self, anchor, num):
                price = int(self.get_price(anchor, num).text.split()[-2])
                name = self.get_item_name(anchor, num)
                return Item(self.driver, name, price)
        
        # Добавление товара в тестовую карзину объекта главной страницы
        def add_to_cart_by_popup(self, category, num):
                anchor = self.get_category_value(category) 
                item = self.take_item(anchor, num)
                item.add_item_by_popup()
                self.cart.add_to_cart(item)

        

        

        

