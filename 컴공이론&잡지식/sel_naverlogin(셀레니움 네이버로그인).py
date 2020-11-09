from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from selenium import webdriver
import requests
import time
import datetime
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login')
id = '아이디'
pw = '비밀번호'
driver.execute_script("document.getElementsByName('id')[0].value=\'" + "lkingkongl" + "\'")
# time.sleep(1)
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + "ckd2031615" + "\'")
# time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(1)
driver.find_element_by_id('query').send_keys("호가플레이")

driver.find_element_by_xpath('//*[@id="search_btn"]/span[2]').click()
driver.find_element_by_xpath('//*[@id="web_layer_0"]/dl/dt/a/strong').click()

driver.close() 
last_tab = driver.window_handles[-1]
driver.switch_to.window(window_name=last_tab)

driver.find_element_by_xpath('//*[@id="PlayLink"]').click() #호가플레이클릭

driver.close() 
last_tab = driver.window_handles[-1]
driver.switch_to.window(window_name=last_tab)

driver.find_element_by_xpath('//*[@id="group"]/a/img').click() #네이버로그인클릭

driver.find_element_by_xpath('//*[@id="PlayLink"]').click() #호가플레이클릭
time.sleep(3)

driver.close() 
last_tab = driver.window_handles[-1]
driver.switch_to.window(window_name=last_tab)

driver.find_element_by_xpath('//*[@id="NameInput"]').send_keys("삼성전기")
driver.find_element_by_xpath('//*[@id="NameButton"]/i').click() #종목선택


html = driver.page_source
soup = BeautifulSoup(html)

BuyQuanity1 = soup.find(id='BuyQuanity1').text
print(BuyQuanity1)
print("\n-------")