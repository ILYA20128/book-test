################################## 2.Registration_login: регистрация аккаунта #########################################
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# 1 Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
# 2 Нажмите на вкладку "My Account Menu"
my_account_one = driver.find_element(By.XPATH, '//a[@href="https://practice.automationtesting.in/my-account/"]')
my_account_one.click()
time.sleep(3)
# 3 В разделе "Register", введите email для регистрации
register_email = driver.find_element(By.ID, "reg_email")
register_email.send_keys("ilya.simonchic@bk.ru")
# 4 В разделе "Register", введите пароль для регистрации
# - составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# - почту и пароль сохраните, потребуются в дальнейшем
register_password = driver.find_element(By.ID, "reg_password")
register_password.send_keys("k0rA3V880N91ttv")
# 5 Нажмите на кнопку "Register"
register_btn = driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[2]/form/p[3]/input[3]')
register_btn.click()
driver.quit()

#################################### 3.Registration_login: логин в систему ############################################
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# # 1 Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# time.sleep(3)
# # 2 Нажмите на вкладку "My Account Menu"
# my_account_two = driver.find_element(By.XPATH, '//a[@href="https://practice.automationtesting.in/my-account/"]')
# my_account_two.click()
# # 3 В разделе "Login", введите email для логина
# username = driver.find_element(By.XPATH, '//*[@id="username"]')
# username.send_keys("ilya.simonchic@bk.ru")
# # 4 В разделе "Login", введите пароль для логина
# password = driver.find_element(By.XPATH, '//*[@id="password"]')
# password.send_keys("k0rA3V880N91ttv")
# # 5 Нажмите на кнопку "Login"
# login_btn = driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
# login_btn.click()
# # 6 Добавьте проверку, что на странице есть элемент "Logout"
# logout_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a'), "Logout"))
# driver.quit()
