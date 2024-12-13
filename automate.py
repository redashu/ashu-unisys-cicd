from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# we are only import webdriver from entire selenium 

# loading particular driver of browser 
# initilizing web driver 
chrome_driver = webdriver.Chrome()
# opening a web url 
chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")

# Selenium can find elements by number of things 
# name , classname  , id , cssSelector , xpath 
#chrome_driver.find_element(By.NAME,"name").send_keys("ashutoshh")
chrome_driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("ashutoshh")
chrome_driver.find_element(By.NAME,"email").send_keys("ashutoshh@linux.com")
chrome_driver.find_element(By.ID,"exampleInputPassword1").send_keys("HelloCloud@123")
# click the box 
chrome_driver.find_element(By.ID,"exampleCheck1").click()
# doing selection in element values 
my_select = Select(chrome_driver.find_element(By.ID,"exampleFormControlSelect1"))
# we can select data by index , visible text as well
my_select.select_by_index(1)
#my_select.select_by_visible_text("Female")
# using css_selector for radio button 
chrome_driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
# using xpath for complex pattern matching 
chrome_driver.find_element(By.XPATH,"//input[@type='submit']").click()
# find the message data 
message = chrome_driver.find_element(By.CLASS_NAME,"alert-success").text

time.sleep(4)


# printnt message
print(message)
# message validation  using assertion in python 
assert "Success" in message
# printing title 
print("page title : ",chrome_driver.title)
# current url 
print("page URL  : ",chrome_driver.current_url)
# saving screenshot 
chrome_driver.save_screenshot("pagehome1.png")
print("current page screenshot saved")
# closing my driver / stopping  
chrome_driver.quit()


