from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Base:

        def __init__(self, driver : webdriver):
                self.driver = driver

        '''Method GET current URL'''
        def grt_current_url(self):
                get_url = self.driver.current_url
                print(f'Current URL : {get_url}')

        '''Method assert words'''
        def assert_words(self, word, result):
                value_word = word.text
                assert value_word == result

        '''Method assert URL'''
        def assert_url(self, result):
                get_url = self.driver.current_url
                assert get_url == result

        '''Method get element'''
        def get_element(self, xpath = None, css = None):
                if xpath:
                        return WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                elif css:
                        return WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located((By.CSS_SELECTOR, xpath)))
