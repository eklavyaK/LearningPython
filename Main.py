import time
import pyautogui
from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\MY PC\OneDrive\Desktop\Apps\chromedriver.exe')
driver.get('https://play.typeracer.com/?universe=lang_hi')

time.sleep(15)
pyautogui.hotkey('ctrl', 'alt', 'i')
time.sleep(2)

text = driver.find_element_by_class_name("gameView").text
text = text.split("\n")
print(type(text))
print(text[-3])
time.sleep(23)

pyautogui.typewrite(text[-3], interval=0.05)

