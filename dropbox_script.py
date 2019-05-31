import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USERNAME = "abv@gmail.com"
PASSWORD = "abcdefgh"

browser = webdriver.Chrome(executable_path="/home/nimish/PycharmProjects/so/internship/macroproject/chromedriver")
browser.get("https://www.dropbox.com/home/bbcfirstwebsite/")
time.sleep(2)
browser.find_elements_by_class_name("sign-in-text")[0].click()
browser.switch_to_window(browser.window_handles[-1])
browser.find_element_by_id("identifierId").send_keys(USERNAME)
browser.find_element_by_id("identifierId").send_keys(Keys.RETURN)
time.sleep(2.5)
browser.find_element_by_name("password").send_keys(PASSWORD)
browser.find_element_by_name("password").send_keys(Keys.RETURN)
while "dropbox.com" not in browser.current_url:
        browser.switch_to_window(browser.window_handles[-1])

while True:
    browser.switch_to_window(browser.window_handles[-1])
    all_elems = browser.find_elements_by_class_name("brws-file-row")
    if all_elems:
        break
for i in all_elems:
    print(i.find_element_by_class_name("brws-file-name-cell-filename").text)
    if i.find_element_by_class_name("brws-file-name-cell-filename").text == "images":
        print(i)
        i.find_element_by_class_name("mc-icon-template-actionable").click()
        break
i.find_element_by_class_name("action-download").click()

ds = "f-KS6Mn4phcAAAAAAAAA3NzNFkI-p_R-83ME5FYuMCSP9RcVn-DoGnp3gcy1-lui"
