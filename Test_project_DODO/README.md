# Чтобы запустить тест нужно выполнить следующие шаги:

1. Установите Python: Посетите официальный веб-сайт Python (**[https://www.python.org](https://www.python.org/)**) и загрузите и установите последнюю версию Python согласно инструкциям, соответствующим вашей операционной системе.
2. Установите библиотеку PyTest, если еще не установлена. Выполните команду в командной строке: `pip3 install pytest`
3. Установите библиотеку Selenium: Выполните команду **`pip3 install selenium`** в командной строке для установки библиотеки Selenium.
4. Установите драйвер браузера Chrome: Если вы планируете использовать браузер Chrome, вам понадобится драйвер Chrome. Вы можете загрузить соответствующую версию драйвера Chrome для вашего браузера с официального репозитория Chromium (**[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)**). Убедитесь, что выбрали версию драйвера, совместимую с вашей установленной версией Chrome.

# Аннотация

## Класс **Base**

Внутри класса определены следующие методы:

- **`grt_current_url()`**: Метод для получения текущего URL и вывода его на консоль.
- **`assert_words(word, result)`**: Метод для сравнения текста элемента с ожидаемым результатом. Принимает два параметра: **`word`** (элемент) и **`result`** (ожидаемый результат). Если текст элемента не соответствует ожидаемому результату, будет вызвано исключение.
- **`assert_url(result)`**: Метод для проверки текущего URL с ожидаемым результатом. Принимает один параметр: **`result`** (ожидаемый результат). Если текущий URL не совпадает с ожидаемым результатом, будет вызвано исключение.
- **`get_element(xpath=None, css=None)`**: Метод для получения элемента на странице. Принимает два необязательных параметра: **`xpath`** и **`css`**, определяющие способ поиска элемента. Метод использует ожидание видимости элемента с помощью **`WebDriverWait`** и возвращает найденный элемент.

## Класс **Main_page**

Является подклассом класса **`Base`**
Представляет главную страницу веб-приложения и содержит методы и атрибуты для взаимодействия с ней

Атрибуты класса:

- **`start_url`**: строковая переменная, содержащая URL стартовой страницы.
- **`categoryes`**: словарь, содержащий названия категорий товаров в качестве ключей и соответствующие им якоря в качестве значений.

Методы класса:

- **`price_xpath(anchor, num)`**: метод для получения XPath локатора элемента цены товара на основе заданного якоря (anchor) и порядкового номера товара (num).
- **`item_name_xpath(anchor, num)`**: метод для получения XPath локатора элемента названия товара на основе заданного якоря (anchor) и порядкового номера товара (num).
- **`get_price(anchor, num)`**: метод для получения элемента цены товара на основе заданного якоря (anchor) и порядкового номера товара (num) с использованием метода **`get_element`** из класса-родителя Base.
- **`get_item_name(anchor, num)`**: метод для получения элемента названия товара на основе заданного якоря (anchor) и порядкового номера товара (num) с использованием метода **`get_element`** из класса-родителя Base.
- **`get_category_value(cat_name)`**: метод для получения значения якоря (anchor) для указанной категории товара (cat_name) из словаря **`categoryes`**.
- **`open_page()`**: метод для открытия стартового URL страницы с помощью метода **`get`** веб-драйвера.
- **`take_item(anchor, num)`**: метод для инициализации объекта товара на основе заданного якоря (anchor) и номера товара (num), с получением его цены и названия. Возвращает экземпляр класса **`Item`**.
- **`add_to_cart_by_popup(category, num)`**: метод для добавления товара в тестовую корзину с использованием всплывающего окна. Получает якорь категории товара (category) и номер товара (num), инициализирует объект товара, добавляет его в корзину с помощью методов класса **`Item`** и добавляет в корзину главной страницы с помощью метода **`add_to_cart`** класса **`Cart`**.

## Класс **Cart_siteshit**

Является подклассом класса **`Base`**
Представляет корзину сайта веб-приложения и содержит методы и атрибуты для взаимодействия с корзиной

Атрибуты класса:

- **`cart_button_xpath`**: строковая переменная с XPath локатором кнопки "Открыть корзину".
- **`cart_title_xpath`**: строковая переменная с XPath локатором заголовка корзины.
- **`title_cnt`**: переменная для хранения количества товаров в корзине.
- **`title_price`**: переменная для хранения итоговой стоимости корзины.

Методы класса:

- **`item_name_xpath(num)`**: метод для получения XPath локатора названия товара на основе порядкового номера товара (**`num`**).
- **`item_price_xpath(num)`**: метод для получения XPath локатора цены товара на основе порядкового номера товара (**`num`**).
- **`get_cart_button()`**: метод для получения элемента кнопки "Открыть корзину" с использованием метода **`get_element`** из класса-родителя **`Base`**.
- **`get_cart_title()`**: метод для получения текста заголовка корзины с использованием метода **`get_element`** из класса-родителя **`Base`**.
- **`get_item_name(num)`**: метод для получения элемента названия товара на основе порядкового номера товара (**`num`**) с использованием метода **`get_element`** из класса-родителя **`Base`**.
- **`get_item_price(num)`**: метод для получения элемента цены товара на основе порядкового номера товара (**`num`**) с использованием метода **`get_element`** из класса-родителя **`Base`**.
- **`take_item(num)`**: метод для инициализации объекта товара на основе порядкового номера товара (**`num`**), получения его цены и названия. Возвращает экземпляр класса **`Item`**.
- **`cart_composition()`**: метод для перебора товаров в корзине и добавления их в объект корзины с помощью метода **`add_to_cart`** из класса **`Cart`**.
- **`go_to_cart()`**: метод для открытия корзины, получения информации о количестве товаров и итоговой стоимости, а затем добавления товаров в объект корзины.

## Класс Item

Является подклассом класса **`Base`**
Представляет товар и содержит методы и атрибуты

Атрибуты класса:

- **`driver`**: экземпляр класса **`webdriver.Chrome`**.
- **`name`**: атрибут для хранения названия товара.
- **`price`**: атрибут для хранения цены товара.
- **`name_text`**: атрибут для хранения текста названия товара.

Методы класса:

- **`action_in_popup()`**: метод для выполнения действий во всплывающем окне товара (попапе). Получает название товара в попапе и сравнивает его с сохраненным названием товара. Затем получает кнопку "Выбрать" в попапе, и если это пицца, меняет цену на итоговую цену пиццы. Затем кликает на кнопку "Выбрать" в попапе. Также содержит костыль для обхода выбора адреса достав
- **`add_item_by_popup()`**: метод, который добавляет товар в корзину через попап. Нажимает на название товара, выполняет действия в попапе с помощью метода **`action_in_popup()`**, а затем выводит название товара и его цену в консоль.

Магические методы:

- **`__add__(self, other)`**: магический метод для сложения цен объектов. Принимает другой объект товара или целое число. Если переданный объект является товаром (**`Item`**), то используется его цена для сложения. Возвращает сумму цен товаров.
- **`__radd__(self, other)`**: магический метод для сложения цены объекта с числом. Принимает другой объект товара или целое число. Если переданный объект является товаром (**`Item`**), то используется его цена для сложения. Возвращает сумму переданного числа и цены текущего товара.
- **`__eq__(self, other)`**: магический метод для сравнения товаров. Принимает другой объект товара и проверяет эквивалентность названия и цены обоих товаров. Возвращает **`True`**, если товары эквивалентны, и **`False`** в противном случае.

## Класс Item

Представляет корзину и содержит методы и атрибуты

Методы класса :

1. **`add_to_cart(self, item: Item)`** - добавляет товар в корзину. Принимает экземпляр класса **`Item`** в аргументе **`item`**. Если **`item`** не является экземпляром класса **`Item`**, вызывается исключение **`ValueError`**.
2. **`__eq__(self, other)`** - магический метод для сравнения корзин. Принимает другой объект **`other`** и сравнивает содержимое корзин. Если **`other`** не является экземпляром класса **`Cart`**, вызывается исключение **`ValueError`**. Корзины сравниваются по отсортированным спискам товаров в алфавитном порядке по полю **`name_text`**.
3. **`__len__(self)`** - магический метод, возвращающий количество товаров в корзине.