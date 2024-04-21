from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
def getInfo(url):
    driver.get(url)
    buy_info = driver.find_elements(By.CLASS_NAME,"buy")
    currency_info = driver.find_elements(By.CLASS_NAME, "currency")
    sell_info = driver.find_elements(By.CLASS_NAME, "sell")
    try:
        print("BUY", end=" ")
        print("CURRENCY", end=" ")
        print("SELL")
        for inf_i in range(len(buy_info)):
            print(buy_info[inf_i].text,end=" ")
            print(currency_info[inf_i].text, end=" ")
            print(sell_info[inf_i].text)
    except:
        print('nothing')
url = "https://www.mig.kz/"
getInfo(url)
