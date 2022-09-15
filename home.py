import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# 1 Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
# 2 Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
# 3 Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
ruby = driver.find_element(By.XPATH, '//img[@title="Selenium Ruby"]')
ruby.click()
# 4 Нажмите на вкладку "REVIEWS"
reviews = driver.find_element(By.XPATH, '//a[@href="#tab-reviews"]')
reviews.click()
# 5 Поставьте 5 звёзд
star = driver.find_element(By.XPATH, '//*[@id="commentform"]/p[2]/p/span/a[5]')
star.click()
# 6 Заполните поле "Review" сообщением: "Nice book!"
review = driver.find_element(By.ID, "comment")
review.send_keys("Nice book!")
# 7 Заполните поле "Name"
autor = driver.find_element(By.ID, "author")
autor.send_keys("Ilya_2022")
# 8 Заполните "Email"
email = driver.find_element(By.ID, "email")
email.send_keys("ilya.simonchic@bk.ru")
# 9 Нажмите на кнопку "SUBMIT"
submit = driver.find_element(By.XPATH, '//*[@id="submit"]')
submit.click()
driver.quit()
