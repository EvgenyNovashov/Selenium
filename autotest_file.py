from selenium import webdriver
import os

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

input1 = browser.find_element_by_name('firstname')
input1.send_keys('Evgen')
input1 = browser.find_element_by_name('lastname')
input1.send_keys('Nov')
input1 = browser.find_element_by_name('email')
input1.send_keys('Evgen@mail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

element = browser.find_element_by_name('file')
element.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()

