from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.firefox import GeckoDriverManager
# Python Selenium SELECT class - It is used for Dropdowns and to select multiple things
from selenium.webdriver.support.ui import Select


class Suman:
    url = 'https://www.imdb.com/search/title/'
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def __init__(self):
        print('Initialization - Success')
        self.driver.maximize_window()
        self.driver.get(self.url)

    # Click the User Rating Dropdown using Python Selenium

    def user_rating(self):
        sleep(4)
        user_rating = self.driver.find_element(
            by=By.NAME, value='user_rating-min')
        sleep(2)
        user_rating.click()

    # Select the Rating from the User rating Dropdown using Python Selenium

    def select_user_rating(self):
        print('Method - select_user_ratin')
        sleep(3)
        user_rating = self.driver.find_element(
            by=By.NAME, value='user_rating-min')
        user_rating_dropdown = Select(user_rating)
        user_rating_dropdown.select_by_visible_text('9.0')

    def select_by_language(self):
        print('Method - select_by_language')
        sleep(2)
        language = self.driver.find_element(by=By.NAME, value='languages')
        language_dropdown = Select(language)
        language_dropdown.select_by_value('bn')


# Suman().select_user_rating()
Suman().select_by_language()
