from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("/Users/monishagopal/Library/CloudStorage/GoogleDrive-monishagopal7@gmail.com/My Drive/2-Hustle/1-PyCharm-Programs/2-drivers/chromedriver_mac_arm64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.implicitly_wait(2)
print(driver.title)
#driver.find_element(By.Name, "username").send_keys("Mona")
print("element found")