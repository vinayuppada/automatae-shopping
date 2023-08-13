import pyautogui
import time
from time import sleep
# from tkinter.tix import Select

import tkinter as tk
from tkinter import ttk
 
from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/oversized-women-t-shirt")

driver.maximize_window()

# Wait for the button to be clickable
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-button-28"]')))
button.click()
sleep(5)

wait = WebDriverWait(driver, 10)
button1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="topcartlink"]/a/span[1]')))
button1.click()
sleep(2)

wait = WebDriverWait(driver, 10)
checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="termsofservice"]')))
checkbox.click()
sleep(2)

# checkout button click
wait = WebDriverWait(driver, 10)
button2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]')))
button2.click()
sleep(2)

# guest

wait = WebDriverWait(driver, 10)
button3 = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/button[1]')))
button3.click()
sleep(2)

# first name   //*[@id="BillingNewAddress_FirstName"]
wait = WebDriverWait(driver, 10)
# f = driver.find_element_by_xpath('//*[@id="BillingNewAddress_FirstName"]')
f = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BillingNewAddress_FirstName"]')))
f.send_keys("vinay")
sleep(2)

# last name
wait = WebDriverWait(driver, 10)
l = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BillingNewAddress_LastName"]')))

# l=driver.find_element_by_xpath('//*[@id="BillingNewAddress_LastName"]')
l.send_keys("uppada")
sleep(2)

wait = WebDriverWait(driver, 10)

e = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BillingNewAddress_Email"]')))

# e=driver.find_element_by_xpath('')
e.send_keys("uppadavinayreddy@gmail.com")
sleep(2)

# Handle the dropdown menu using Selenium
wait = WebDriverWait(driver, 10)
country_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BillingNewAddress_CountryId"]')))
country_dropdown.click()

# Find the desired option by its text and click it
option_to_select = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="BillingNewAddress_CountryId"]/option[101]')))
option_to_select.click()

# city    //*[@id="BillingNewAddress_City"]
wait = WebDriverWait(driver, 10)
c = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BillingNewAddress_City"]')))

# l=driver.find_element_by_xpath('//*[@id="BillingNewAddress_LastName"]')
c.send_keys("visakhapatnam")
sleep(2)

# address1
wait = WebDriverWait(driver, 10)
c = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BillingNewAddress_Address1"]')))

# l=driver.find_element_by_xpath('//*[@id="BillingNewAddress_LastName"]')
c.send_keys("dighi hills")
sleep(2)

# zip   //*[@id="BillingNewAddress_ZipPostalCode"]
wait = WebDriverWait(driver, 10)
z = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BillingNewAddress_ZipPostalCode"]')))

# l=driver.find_element_by_xpath('//*[@id="BillingNewAddress_LastName"]')
z.send_keys("411015")
sleep(2)

# phone    //*[@id="BillingNewAddress_PhoneNumber"]
wait = WebDriverWait(driver, 10)
z = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BillingNewAddress_PhoneNumber"]')))

# l=driver.find_element_by_xpath('//*[@id="BillingNewAddress_LastName"]')
z.send_keys("7287936138")
sleep(2)

# contnue   //*[@id="billing-buttons-container"]/button[4]
wait = WebDriverWait(driver, 10)
button4 = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="billing-buttons-container"]/button[4]')))
button4.click()
sleep(5)

# ground select
wait = WebDriverWait(driver, 10)
ground = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shippingoption_0"]')))
ground.click()
sleep(2)

# continue   //*[@id="shipping-method-buttons-container"]/button
wait = WebDriverWait(driver, 10)
button5 = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="shipping-method-buttons-container"]/button')))
button5.click()
sleep(2)

# debit card   //*[@id="paymentmethod_0"]
wait = WebDriverWait(driver, 10)
payment = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="paymentmethod_0"]')))
payment.click()
sleep(2)

# continue
wait = WebDriverWait(driver, 10)
button6 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="payment-method-buttons-container"]/button')))
button6.click()
sleep(2)

# continue   //*[@id="payment-info-buttons-container"]/button
wait = WebDriverWait(driver, 10)
button7 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="payment-info-buttons-container"]/button')))
button7.click()
sleep(2)

# continue  //*[@id="confirm-order-buttons-container"]/button

wait = WebDriverWait(driver, 10)
button8 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="confirm-order-buttons-container"]/button')))
button8.click()
sleep(2)

# order no /html/body/div[6]/div[3]/div/div/div/div[2]/div/div[2]/div[1]/strong
# click here for more details   /html/body/div[6]/div[3]/div/div/div/div[2]/div/div[2]/div[2]/a
wait = WebDriverWait(driver, 10)
button9 = wait.until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div/div[2]/div[2]/a')))
button9.click()
sleep(2)

# print /html/body/div[6]/div[3]/div/div/div/div[1]/a[1]
wait = WebDriverWait(driver, 10)
button10 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[1]/a[1]')))
button10.click()
# driver.switch_to_alert().accept()  # pdf is saved
try:
    alert = driver.switch_to.alert
    alert.dismiss()  # Accept the alert (click OK)
except NoAlertPresentException:
    # If there is no alert, handle the exception
    pass


sleep(2)

# save in the alert


# after the saving the pdf in the pc wait for to see the order details in the screen

#disable click
# actions = ActionChains(driver)
# actions.move_by_offset(1237, 616).click().perform()


time.sleep(1)  # Wait for the print dialog to open
pyautogui.press('esc')  # Confirm the print action


sleep(10)

driver.quit()  # Use quit() to close the browser properly
