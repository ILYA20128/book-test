################################################ 4.Shop: отображение страницы товара ###################################
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

#1 Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
time.sleep(3)
#2 Залогиньтесь
my_account_one = driver.find_element(By.XPATH, '//a[@href="https://practice.automationtesting.in/my-account/"]')
my_account_one.click()
username = driver.find_element(By.XPATH, '//*[@id="username"]')
username.send_keys("ilya.simonchic@bk.ru")
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("k0rA3V880N91ttv")
login_btn = driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
login_btn.click()
#3 Нажмите на вкладку "Shop"
shop_btn = driver.find_element(By.XPATH, '//*[@id="menu-item-40"]/a')
shop_btn.click()
#4 Откройте книгу "HTML 5 Forms"
book = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[3]/a[1]')
book.click()
#5 Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
book_text = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="product-181"]/div[2]/h1'), "HTML5 Forms"))
driver.quit()

########################################## 5.Shop: количество товаров в категории ######################################
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# #1 Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# time.sleep(3)
# #2 Залогиньтесь
# my_account_one = driver.find_element(By.XPATH, '//a[@href="https://practice.automationtesting.in/my-account/"]')
# my_account_one.click()
# username = driver.find_element(By.XPATH, '//*[@id="username"]')
# username.send_keys("ilya.simonchic@bk.ru")
# password = driver.find_element(By.XPATH, '//*[@id="password"]')
# password.send_keys("k0rA3V880N91ttv")
# login_btn = driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
# login_btn.click()
# #3 Нажмите на вкладку "Shop"
# shop_btn = driver.find_element(By.XPATH, '//*[@id="menu-item-40"]/a')
# shop_btn.click()
# #4 Откройте категорию "HTML"
# category_html = driver.find_element(By.XPATH, '//*[@id="woocommerce_product_categories-2"]/ul/li[2]/a')
# category_html.click()
# time.sleep(3)
# #5 Добавьте тест, что отображается три товара
# books_list = driver.find_elements(By.XPATH, '//*[@id="content"]/ul/li')
# if len(books_list) == 3:
#     print("В списке 3 книги")
# else:
#     print("Ошибка. В списке: " + str(len(books_list)))
# driver.quit()

############################################# 6.Shop: сортировка товаров  ##############################################
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# #1 Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# time.sleep(3)
# #2 Залогиньтесь
# my_account_one = driver.find_element(By.XPATH, '//a[@href="https://practice.automationtesting.in/my-account/"]')
# my_account_one.click()
# username = driver.find_element(By.XPATH, '//*[@id="username"]')
# username.send_keys("ilya.simonchic@bk.ru")
# password = driver.find_element(By.XPATH, '//*[@id="password"]')
# password.send_keys("k0rA3V880N91ttv")
# login_btn = driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
# login_btn.click()
# #3 Нажмите на вкладку "Shop"
# shop_btn = driver.find_element(By.XPATH, '//*[@id="menu-item-40"]/a')
# shop_btn.click()
# #4 Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# default_sorting = driver.find_element(By.XPATH, '//*[@id="content"]/form/select/option[1]')
# value_check = WebDriverWait(driver, 5).until(EC.element_to_be_selected(default_sorting))
# #5 Отсортируйте товары по цене от большей к меньшей
# sort_btn = driver.find_element(By.XPATH, '//*[@id="content"]/form/select')
# sort_btn.click()
# sort_price = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/form/select/option[6]')
# sort_price.click()
# #6 Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# sort_btn = driver.find_element(By.XPATH, '//*[@id="content"]/form/select')
# sort_btn.click()
# # #7 Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# sort_of_price = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/form/select/option[6]')
# low_check = WebDriverWait(driver, 5).until(EC.element_to_be_selected(sort_of_price))
# driver.quit()
############################################# 7.Shop: отображение, скидка товара  ######################################
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# #1 Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# time.sleep(3)
# #2 Залогиньтесь
# my_account_one = driver.find_element(By.XPATH, '//a[@href="https://practice.automationtesting.in/my-account/"]')
# my_account_one.click()
# username = driver.find_element(By.XPATH, '//*[@id="username"]')
# username.send_keys("ilya.simonchic@bk.ru")
# password = driver.find_element(By.XPATH, '//*[@id="password"]')
# password.send_keys("k0rA3V880N91ttv")
# login_btn = driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
# login_btn.click()
# #3 Нажмите на вкладку "Shop"
# shop_btn = driver.find_element(By.XPATH, '//*[@id="menu-item-40"]/a')
# shop_btn.click()
# #4 Откройте книгу "Android Quick Start Guide"
# book_anroid_guide = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[1]/a[1]')
# book_anroid_guide.click()
# #5 Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
# #6 Добавьте тест, что содержимое новой цены = "₹450.00"  # используйте assert
# old_price = driver.find_element(By.CSS_SELECTOR, ".price > del > span")
# old_price_text = old_price.text
# new_price = driver.find_element(By.CSS_SELECTOR, ".price > ins > span")
# new_price_text = new_price.text
# assert old_price_text == "₹600.00"
# assert new_price_text == "₹450.00"
# #7 Добавьте явное ожидание и нажмите на обложку книги
# # - Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
# cover_book = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# cover_book.click()
# #8 Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
# cover_book_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# cover_book_close.click()
# driver.quit()

############################################# 8.Shop: проверка цены в корзине  ########################################
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# # 1 Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# driver.get("http://practice.automationtesting.in/")
# time.sleep(3)
# # 2 Нажмите на вкладку "Shop"
# shop_btn = driver.find_element(By.XPATH, '//*[@id="menu-item-40"]/a')
# shop_btn.click()
# # 3 Добавьте в корзину книгу "HTML5 WebApp Development"
# book_html5 = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[4]/a[2]')
# book_html5.click()
# time.sleep(3)
# # 4 Добавьте тест, что возле корзины(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# numbers_of_items = driver.find_element(By.CSS_SELECTOR, ".cartcontents")
# numbers_of_items_text = numbers_of_items.text
# amount = driver.find_element(By.XPATH, '//*[@id="wpmenucartli"]/a/span[2]')
# amount_text = amount.text
# assert numbers_of_items_text == "1 Item"
# assert amount_text == "₹180.00"
# time.sleep(3)
# # 5 Перейдите в корзину
# basket = driver.find_element(By.XPATH, '//*[@id="wpmenucartli"]/a/i')
# basket.click()
# # 6 Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# subtotal_price_check = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-34"]/div/div[1]/div/div/table/tbody/tr[1]/td/span'),
#                                      "₹"))
# # 7 Используя явное ожидание, проверьте что в Total отобразилась стоимость
# total_amout_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
#     (By.XPATH, '//*[@id="page-34"]/div/div[1]/div/div/table/tbody/tr[3]/td/strong/span'), "₹"))

############################################# 9.Shop: работа в корзине  ###############################################
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.maximize_window()
# #1 Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# driver.get("http://practice.automationtesting.in/")
# time.sleep(3)
# #2 Нажмите на вкладку "Shop"
# shop_btn = driver.find_element(By.XPATH, '//*[@id="menu-item-40"]/a')
# shop_btn.click()
# #3 Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# # - Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# # - После добавления 1-й книги добавьте sleep
# driver.execute_script("window.scrollBy(0, 300);")
# html_book = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[4]/a[2]')
# html_book.click()
# time.sleep(3)
# js_book = driver.find_element(By.XPATH, '//html/body/div[1]/div[2]/div/div/ul/li[5]/a[2]')
# js_book.click()
# time.sleep(3)
# #4 Перейдите в корзину
# basket = driver.find_element(By.XPATH, '//*[@id="wpmenucartli"]/a/i')
# basket.click()
# #5 Удалите первую книгу
# # - Перед удалением добавьте sleep
# time.sleep(3)
# remove_book = driver.find_element(By.XPATH, '//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[1]/a')
# time.sleep(3)
# remove_book.click()
# time.sleep(3)
# #6 Нажмите на Undo (отмена удаления)
# # undo_btn = driver.find_element(By.XPATH, '//*[@id="page-34"]/div/div[1]/div[1]/a')
# undo_btn = driver.find_element(By.LINK_TEXT, "Undo?")
# undo_btn.click()
# #7 В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# # - Предварительно очистите поле с помощью локатор_поля.clear()
# quantity = driver.find_element(By.XPATH, '//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input')
# quantity.clear()
# quantity.send_keys("3")
# #8 Нажмите на кнопку "UPDATE BASKET"
# submit_btn = driver.find_element(By.NAME, "update_cart")
# submit_btn.click()
# #9 Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
# qty = driver.find_element(By.XPATH, '//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input')
# qty_status_started = qty.get_attribute("value")
# if qty_status_started == "3":
#     print("Количество книг = 3")
# else:
#     print("Количество книг: ", qty_status_started)
# #10 Нажмите на кнопку "APPLY COUPON"
# # - Перед нажатием добавьте sleep
# time.sleep(3)
# coupon = driver.find_element(By.NAME, "apply_coupon")
# coupon.click()
# #11 Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# total_amout_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
#     (By.CSS_SELECTOR, ".woocommerce-error"), "Please enter a coupon code."))
# driver.quit()

############################################# 10.Shop: покупка товара  ###############################################
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# # 1 Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# driver.get("http://practice.automationtesting.in/")
# time.sleep(3)
# # 2 Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
# shop_btn = driver.find_element(By.XPATH, '//*[@id="menu-item-40"]/a')
# shop_btn.click()
# driver.execute_script("window.scrollBy(0, 300);")
# # 3 Добавьте в корзину книгу "HTML5 WebApp Development"
# html_book = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[4]/a[2]')
# html_book.click()
# time.sleep(3)
# # 4 Перейдите в корзину
# basket = driver.find_element(By.XPATH, '//*[@id="wpmenucartli"]/a/i')
# basket.click()
# # 5 Нажмите "PROCEED TO CHECKOUT"
# # - Перед нажатием, добавьте явное ожидание
# checkout_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="page-34"]/div/div[1]/div/div/div/a')))
# checkout_btn.click()
# # 6 Заполните все обязательные поля
# # - Перед заполнением first name, добавьте явное ожидание
# # - Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# # - Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
# first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
# first_name.send_keys("Ronni")
# last_name = driver.find_element(By.ID, "billing_last_name")
# last_name.send_keys("Koliman")
# email = driver.find_element(By.ID, "billing_email")
# email.send_keys("ilya.simonchic@bk.ru")
# phone = driver.find_element(By.ID, "billing_phone")
# phone.send_keys("1234567890")
# country_list = driver.find_element(By.ID, "s2id_billing_country")
# country_list.click()
# search = driver.find_element(By.XPATH, '//*[@id="s2id_autogen1_search"]')
# search.send_keys("Russia")
# russia_btn = driver.find_element(By.CSS_SELECTOR, ".select2-match")
# russia_btn.click()
# address = driver.find_element(By.XPATH, '//*[@id="billing_address_1"]')
# address.send_keys("10 First Freeway")
# town_city = driver.find_element(By.NAME, "billing_city")
# town_city.send_keys("Id nisi itaque dign")
# state_county = driver.find_element(By.NAME, "billing_state")
# state_county.send_keys("Placeat in laudanti")
# postcode = driver.find_element(By.NAME, "billing_postcode")
# postcode.send_keys("14597")
# # 7 Выберите способ оплаты "Check Payments"
# # - Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(2)
# check_payments = driver.find_element(By.XPATH, '//*[@id="payment_method_cheque"]')
# check_payments.click()
# time.sleep(3)
# # 8 Нажмите PLACE ORDER
# place_order = driver.find_element(By.XPATH, '//*[@id="place_order"]')
# place_order.click()
# # 9 Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
# woocomerce = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),
#                                      "Thank you. Your order has been received."))
# # 10 Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
# check_pay = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method"), "Check Payments"))
# driver.quit()