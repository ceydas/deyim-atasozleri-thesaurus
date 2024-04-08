from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()
USER_AGENT = os.getenv("USER_AGENT")
HEADERS = ({'User-Agent':USER_AGENT, 'Accept-Language': 'en-US, en;q=0.5'})

#TDK Atasözleri & Deyimler Web URL
URL = "https://sozluk.gov.tr/?q=&aranan="

def tdk_scrape_atasozleri_deyimler():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    
    dict_selector = driver.find_element(by= By.XPATH, value="//button[@id='btn11']")
    dict_selector.click()

    ad_checkbox = driver.find_element(by= By.XPATH, value="//input[@name='ads']")
    ad_checkbox.click()

    general_dict_checkbox = driver.find_element(by=By.XPATH, value="//input[@id='gts']")
    if general_dict_checkbox.is_selected:
        general_dict_checkbox.click() #uncheck the checkbox.


    tdk_search_btn = driver.find_element(by=By.ID, value="tdk-search-btn")
    tdk_search_btn.click() #search 

    #driver.quit()

tdk_scrape_atasozleri_deyimler()
