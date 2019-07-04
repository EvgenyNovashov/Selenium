from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def calc2(x,y):
  return str(int(x)+int(y))

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

element_x = browser.find_element_by_css_selector("#num1")
x = element_x.text
element_y = browser.find_element_by_css_selector("#num2")
y = element_y.text

z = calc2(x,y)

browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("[value='" + z + "']").click()


# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
