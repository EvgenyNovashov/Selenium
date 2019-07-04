from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
#input1 = browser.find_element_by_css_selector(".first_block .first")
#input1.send_keys("Ivan")
#input2 = browser.find_element_by_css_selector(".first_block .second")
#input2.send_keys("Ivanov")
#input3 = browser.find_element_by_css_selector(".first_block .third")
#input3.send_keys("mail@mail.ru")

#input1 = browser.find_element_by_xpath("//input[@placeholder='Введите имя']")
#input1.send_keys("Ivan")
#input2 = browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']")
#input2.send_keys("Petrov")
#input3 = browser.find_element_by_xpath("//input[@placeholder='Введите Email']")
#input3.send_keys("1@gmail.com")


name_input = browser.find_element_by_css_selector("div.first_block input.first")
name_input.send_keys("name")
surname_input = browser.find_element_by_css_selector("div.first_block input.second")
surname_input.send_keys("surname")
email_input = browser.find_element_by_css_selector("div.first_block input.third")
email_input.send_keys("email")



# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(2)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text