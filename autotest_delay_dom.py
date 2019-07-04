from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
#opt = webdriver.ChromeOptions()
#opt.add_experimental_option('w3c', False)
#browser = webdriver.Chrome(chrome_options=opt)
browser.get("http://suninjuly.github.io/explicit_wait2.html")
#time.sleep(1)
#button = browser.find_element_by_id("check")

#button = WebDriverWait(browser, 12).until(
#        EC.element_to_be_clickable((By.ID, "check"))
#    )

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"10000 RUR")
    )

button = browser.find_element_by_id("book")
button.click()

element_x = browser.find_element_by_css_selector(".container #input_value")
x = element_x.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

button = browser.find_element_by_id("solve")
button.click()

