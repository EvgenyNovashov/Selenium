from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#link = "http://suninjuly.github.io/math.html"
link = "http://suninjuly.github.io/get_attribute.html"
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

#name_input = browser.find_element_by_css_selector("div.first_block input.first")
#name_input.send_keys("name")
#surname_input = browser.find_element_by_css_selector("div.first_block input.second")
#surname_input.send_keys("surname")
#email_input = browser.find_element_by_css_selector("div.first_block input.third")
#email_input.send_keys("email")


#element_x = browser.find_element_by_css_selector(".container #input_value")
#x = element_x.text
element_x = browser.find_element_by_css_selector("img#treasure")
x = element_x.get_attribute("valuex")

y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()
option3 = browser.find_element_by_id("robotsRule")
option3.click()

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
