from selenium import webdriver
from math import (log,sin)

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = int(browser.find_element_by_css_selector('span#input_value.nowrap').text)

inputField = browser.find_element_by_css_selector("input#answer.form-control")
inputField.send_keys(str(log(abs(12*sin(x)))))

button2 = browser.find_element_by_css_selector("button.btn.btn-primary")
button2.click()




