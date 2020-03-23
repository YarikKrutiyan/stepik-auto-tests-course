from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import (log,sin)

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

# price = browser.find_element_by_css_selector("h5#price").text

price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), '100')
    )

book = browser.find_element_by_css_selector("button#book.btn.btn-primary")
book.click()


x = int(browser.find_element_by_css_selector('span#input_value.nowrap').text)


inputF = browser.find_element_by_css_selector('input#answer.form-control')
inputF.send_keys(str(log(abs(12*sin(x)))))


# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()


btn2 = browser.find_element_by_css_selector('button#solve.btn-primary')
btn2.click()