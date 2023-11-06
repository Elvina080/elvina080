import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from pages.Cart_siteshit import Cart_siteshit
from pages.Main_page import Main_page




def test_smoke_1():
        
        print('Start')

        # Список категорий для проверки
        categories = ['pizza', 'snack', 'coctail', 'drink']

        # Инициализация вебдрайвера, чтобы окно не закрывалось
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=Service())
        
        # Открытие главной страницы
        main_page = Main_page(driver)
        main_page.open_page()

        # Перебор тестовых категорий
        for category in categories:
                # Добавление по одному товару из категории в карзину
                try:
                        main_page.add_to_cart_by_popup(category, 1)
                        print('Добавлен в карзину')
                except Exception:
                        print('Не добавлен в карзину')
                        continue
        print(f'Товары на сумму : {sum(main_page.cart.cart)}')

        # Открытие сайтшита карзины
        cart_siteshit = Cart_siteshit(driver)
        cart_siteshit.go_to_cart()
        print(f'Сумма в карзине : {sum(cart_siteshit.cart.cart)}')

        # Сравнение карзин через магический метод
        assert  main_page.cart == cart_siteshit.cart    
        # Сравнение кол-ва товаров в карзинах 
        assert len(main_page.cart) == len(cart_siteshit.cart)
        # Сравнение итоговых сумм
        assert sum(main_page.cart.cart) == sum(cart_siteshit.cart.cart)

        print('Товары, добавленные в карзину совпадают с товарами в карзине')
        print('Успешный тест')        
        time.sleep(10)
        driver.quit()

