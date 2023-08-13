import pyautogui
import time

from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get('https://www.thoughtco.com/how-to-add-a-print-button-4072006')

driver.maximize_window()
# Create an ActionChains instance

wait = WebDriverWait(driver, 10)
button8 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="print-button_1-0"]/button')))
button8.click()
sleep(4)


# actions = ActionChains(driver)

# element = driver.find_element(By.ID, "relative-location")
# actions.move_to_element(element).perform()
# #
# element = driver.find_element(By.ID, "element_id")
# actions.click_and_hold(element).perform()
# actions.release().perform()
# element = driver.find_element(By.ID, "click")
# actions.double_click(element).perform()
# source_element = driver.find_element(By.ID, "source_id")
# target_element = driver.find_element(By.ID, "target_id")
# actions.drag_and_drop(source_element, target_element).perform()

# actions.move_by_offset(1232, 613).click().perform()
# actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

# button8 = driver.switch_to.active_element
# driver.find_element_by_id('print_button_id').click()
# button8.send_keys(Keys.ESCAPE)



# driver.execute_script("document.exitFullscreen();")



time.sleep(1)  # Wait for the print dialog to open
pyautogui.press('esc')  # Confirm the print action



sleep(5)

# Close the browser
driver.quit()
