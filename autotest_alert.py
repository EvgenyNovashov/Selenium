from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = " http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_css_selector("button.btn")
button.click()


prompt = browser.switch_to.alert
#prompt.send_keys("My answer")
prompt.accept()

element_x = browser.find_element_by_css_selector(".container #input_value")
x = element_x.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()
