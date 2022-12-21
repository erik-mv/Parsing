from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://gb.ru/login')

elem = driver.find_element(By.ID, 'user_email')
elem.send_keys('mabemi6344@oncebar.com')
elem = driver.find_element(By.ID, 'user_password')
elem.send_keys('test1234')
elem.send_keys(Keys.ENTER)

#elem = driver.find_element(By.CLASS_NAME, 'mn-dropdown-item__link')
elem = driver.find_element(By.XPATH, "//div[@class='mn-dropdown mn-dropdown__profile mn-dropdown_position-right']//a")
profile_link = elem.get_attribute('href')
driver.get(profile_link)

elem = driver.find_element(By.CLASS_NAME, 'text-sm')
edit_profile_link = elem.get_attribute('href')
driver.get(edit_profile_link)

timezone = driver.find_element(By.NAME, "user[time_zone]")
select = Select(timezone)
select.select_by_value("Volgograd")
timezone.submit()

print()