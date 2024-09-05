import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://pubmed.ncbi.nlm.nih.gov/')
driver.find_element(By.ID,'id_term').send_keys('taraxacum officinale')
driver.find_element(By.CLASS_NAME,"search-btn").click()
driver.get(driver.current_url)
lst = driver.find_elements(By.CLASS_NAME, 'docsum-title')
for i in range(len(lst)):
    driver.find_elements(By.CLASS_NAME, 'docsum-title')[i].click()
    driver.back()
time.sleep(5)
