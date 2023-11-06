
from selenium import webdriver

from base.Base_class import Base

class Item(Base):


        '''Класс товара'''
        def __init__(self, driver: webdriver.Chrome, name, price : int):
                '''Создание объекта товара'''
                self.driver = driver
                self.name = name 
                self.price = price
                self.name_text = name.text
                

        # Locators

        # popup (локаторы товара пиццы и остальных товаров отличаются)

        # Название товара в попапе
        popup_pizza_name_xpath = '/html/body/div[5]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/h1' # У попапа пиццы отдельные xpath
        popup_other_name_xpath = '/html/body/div[5]/div/div[2]/div/section/main/h1'
        # Цена товара в попапе (кнопка выбрать)
        popup_pizza_choose_button_price_xpath = '/html/body/div[5]/div/div[2]/div/div/div[2]/div[2]/button/span/span[1]' # У попапа пиццы отдельные xpath
        popup_choose_button_price_xpath = '/html/body/div[5]/div/div[2]/div/section/main/button/span/span[1]'
        

        # Actions

        # Действие в попапе
        def action_in_popup(self):
                # Получение названия товара в попапе
                try:
                        popup_item_name = self.get_element(xpath=self.popup_other_name_xpath)
                except Exception:
                        popup_item_name = self.get_element(xpath=self.popup_pizza_name_xpath)
                assert popup_item_name.text == self.name_text
                
                # Получение кнопки "Выбрать" в попапе
                try:
                        popup_choose_button = self.get_element(xpath=self.popup_choose_button_price_xpath)
                except Exception:
                        popup_choose_button = self.get_element(xpath=self.popup_pizza_choose_button_price_xpath)
                        # Если это пицца -- меняем цену на итоговую
                        self.price = int(popup_choose_button.text)
                popup_choose_button.click()

                # Костыль для обхода выбора адреса доставки
                try:
                        kostyl = self.get_element(xpath='/html/body/div[5]/div[2]/div[2]/div/div/div[2]/button')
                        kostyl.click()
                        kostyl_1 = self.get_element(xpath='/html/body/div[5]/div[2]/div[2]/div/div/form/div[1]/div[3]/button')
                        kostyl_1.click()
                except Exception:
                        pass


        # Открытие попапа и добавление в карзину        
        def add_item_by_popup(self):
                '''Добавление товара в карзину через попап'''
                self.name.click()
                self.action_in_popup()
                print(self.name_text, self.price)

                
                
        # Магические методы

        def __add__(self, other):
                '''Магический метод для сложения цен объектов'''
                if not isinstance(other, (Item, int)):
                        raise TypeError('Метод складывает только объекты или объект с числом')
                x = other
                if isinstance(other, Item):
                        x = other.price
                return self.price + x
        def __radd__(self, other):
                '''Магический метод для сложения суммы с ценой объекта'''
                if not isinstance(other, (Item, int)):
                        raise TypeError('Метод складывает только объекты или объект с числом')
                x = other
                if isinstance(other, Item):
                        x = other.price
                return x + self.price
        
        def __eq__(self, other):
                '''Магический метод для сравнения товаров'''
                if not isinstance(other, Item):
                        raise TypeError('Сравниваются не два товара')
                return self.name_text == other.name_text and self.price == other.price
        
        