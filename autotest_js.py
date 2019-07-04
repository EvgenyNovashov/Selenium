from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
#browser.execute_script("alert('Robots at work');")
#browser.execute_script("document.title='Script executing';alert('Robots at work');")

link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

element_x = browser.find_element_by_css_selector(".container #input_value")
x = element_x.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

option3 = browser.find_element_by_id("robotsRule")
option3.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
#assert True