from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(15) 
driver.get('https://pikabu.ru/community/steam')


for i in range(5):
    articles = driver.find_elements(By.TAG_NAME, "article")
    actions = ActionChains(driver)
    actions.move_to_element(articles[-1])
    actions.perform()
    #actions.click()
    #actions.send_keys("Hello")
    #actions.key_down(Keys.CONTROL).key_up(Keys.CONTROL)

print()