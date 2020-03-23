from selenium import webdriver
from math import (sin,log10,log)


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x = browser.find_element_by_css_selector('span#input_value.nowrap').text
input_field = browser.find_element_by_css_selector('input#answer.form-control')
z = log(abs(12 * sin(int(x))))
input_field.send_keys(str(z))

check_box = browser.find_element_by_css_selector('input#robotCheckbox.form-check-input')
check_box.click()

browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
radio = browser.find_element_by_css_selector('input#robotsRule.form-check-input')
radio.click()

button = browser.find_element_by_css_selector('button.btn.btn-primary')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()




