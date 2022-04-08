
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
s=Service("C:\development\chromedriver.exe")
#smart_chain_address=input('Kindly input your binance block chain address: ')

driver = webdriver.Chrome(service=s)
BINANCE_SMARTCHAIN_ADDRESS="PASTE YOUR ADDRESS HERE"
for n in range(100):
    web_page=driver.get('https://testnet.binance.org/faucet-smart')
    search=driver.find_element(By.XPATH, "//*[@id='url']")
    search.send_keys(BINANCE_SMARTCHAIN_ADDRESS)
    time.sleep(1)
    click=driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/span[1]/button")
    click.click()
    time.sleep(1)
    dropdown=driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/span[1]/ul")
    dropdown.click()
    time.sleep(2)
    message=driver.find_element(By.CLASS_NAME, "noty_message")
    print('runing for {} times '.format(n))
    print(message.text)

driver.quit()


