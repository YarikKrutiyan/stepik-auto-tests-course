from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element_by_css_selector('input:nth-child(2)')
name.send_keys('name')

lastName = browser.find_element_by_css_selector('input:nth-child(4)')
lastName.send_keys('lastname')


email = browser.find_element_by_css_selector('input:nth-child(6)')
email.send_keys('email')

sendFile = browser.find_element_by_css_selector('input#file')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')
sendFile.send_keys(file_path)

b = browser.find_element_by_css_selector('body > div > form > button')
b.click()

