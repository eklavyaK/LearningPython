import time
import pyautogui
from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\MY PC\Desktop\Apps\chromedriver.exe')
driver.get('https://10fastfingers.com/typing-test/english')

time.sleep(10)
for line in range(250):
    text = driver.find_element_by_class_name("highlight").text
    text = text.split("|")
    print(type(text))
    pyautogui.typewrite(text[0], interval=0.05)
    pyautogui.write(' ')





