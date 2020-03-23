from selenium import webdriver
from math import (log,sin)

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

btn = browser.find_element_by_css_selector('button.btn.btn-primary')
btn.click()

alert = browser.switch_to.alert
alert.accept()

x = int(browser.find_element_by_css_selector('span#input_value.nowrap').text)


inputF = browser.find_element_by_css_selector('input#answer.form-control')
inputF.send_keys(str(log(abs(12*sin(x)))))





btn2 = browser.find_element_by_css_selector('button#solve.btn-primary')
btn2.click()