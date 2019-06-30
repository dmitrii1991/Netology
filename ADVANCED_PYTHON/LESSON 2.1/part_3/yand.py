from selenium import webdriver
import time

class Yandex:
    
    def __init__(self, login, password):
        self.login = login
        self.password = password
        
    def auto(self):
        browser = webdriver.Chrome()  # подключаем указатель на браузер
        browser.get('https://passport.yandex.ru/auth/')  # переход на страницу
        # заполнение поля пользователя
        email = browser.find_element_by_id("passp-field-login")
        email.send_keys(self.login)
        # нажимаем на кнопку ввести логин
        submit_email = browser.find_element_by_xpath('//button[@class="control button2 button2_view_classic button2_size_l button2_theme_action button2_width_max button2_type_submit passp-form-button"]')
        submit_email.click()
        time.sleep(2)
        # заполнение пароль
        login = browser.find_element_by_id('passp-field-passwd')
        login.send_keys(self.password)
        # нажимаем на кнопку ввести ПАРОЛЬ
        submit_login = browser.find_element_by_xpath('//button[@class="control button2 button2_view_classic button2_size_l button2_theme_action button2_width_max button2_type_submit passp-form-button"]')
        submit_login.click()

if __name__ == "__main__":
    
    Dima = Yandex('maksimus.maksi', '1ddsd')
    Dima.auto()
