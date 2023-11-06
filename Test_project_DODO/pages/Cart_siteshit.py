
from selenium import webdriver

from utilities.Item_class import Item
from utilities.Cart_class import Cart
from base.Base_class import Base

class Cart_siteshit(Base):

        def __init__(self, driver : webdriver):
                super().__init__(driver)
                self.cart = Cart(self.driver)
                self.title_cnt = None
                self.title_price = None




        # Locators

        cart_button_xpath = '//*[@id="react-app"]/nav/div/div[2]/button'
        cart_title_xpath = '/html/body/div[5]/div/div[2]/div/div/div[1]/main/section[1]/h1'
        
        

        # Конструктор локаторов для товаров

        # Получение локатора названия товара
        def item_name_xpath(self, num):
                return f'/html/body/div[5]/div/div[2]/div/div/div[1]/main/section[2]/article[{num}]/div[2]/div/h3'
        # Получение локатора цены товара
        def item_price_xpath(self, num):
                return f'/html/body/div[5]/div/div[2]/div/div/div[1]/main/section[2]/article[{num}]/div[3]/div[1]/div'


        # Getters

        # Получение элементов

        # Элемент ктопки "Открыть карзину"
        def get_cart_button(self):
                return self.get_element(xpath=self.cart_button_xpath)
        # Элемент заколовка карзины
        def get_cart_title(self):
                return self.get_element(xpath=self.cart_title_xpath).text
        
        
        # Конструктор получения элементов товаров
        
        # Элемент название товара
        def get_item_name(self, num):
                return self.get_element(xpath=self.item_name_xpath(num))
        # Элемент цена твоара
        def get_item_price(self, num):
                return self.get_element(xpath=self.item_price_xpath(num))
        
        
        # Actions

        # Инициализация объекта товара
        def take_item(self, num):
                price = int(self.get_item_price(num).text.split()[-2])
                name = self.get_item_name(num)
                return Item(self.driver, name, price)
        
        # Перебор товаров в карзине и добавление их в объект карзины
        def cart_composition(self):
                for i in range(self.title_cnt):
                        num = i+1
                        item = self.take_item(num)
                        self.cart.add_to_cart(item)
        
        # Открытие карзины 
        def go_to_cart(self):
                cart_button = self.get_cart_button()
                cart_button.click()
                self.title_cnt = int(self.get_cart_title.split()[0]) # количество товаров
                self.title_price = int(self.get_cart_title.split()[-2]) # итоговая стоимость
                self.cart_composition()

        


        
        