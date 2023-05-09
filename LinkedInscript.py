
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

linkedin_username = "yourusernamehere"
linkedin_password = "yourpasswordhere"

data = pd.read_excel("C:/Users/willi/Documents\GitHub\LinkedIn-Script/namelist.xlsx", engine='openpyxl')

def main():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path="C:/Users/willi/Documents\GitHub\LinkedIn-Script/chromedriver.exe", options=options)

    login_to_linkedin(driver)
    input("Press ENTER on CMD after manually logging in...")

    for index, row in data.iterrows():
        perform_search(driver, row['First Name'], row['Last Name'])

    driver.quit()

def login_to_linkedin(driver):
    driver.get('https://www.linkedin.com/login')
    driver.find_element(By.ID, 'username').send_keys(linkedin_username)
    driver.find_element(By.ID, 'password').send_keys(linkedin_password)
    driver.find_element(By.CSS_SELECTOR, '.btn__primary--large').click()

def perform_search(driver, first_name, last_name):
    search_url = f'https://www.linkedin.com/search/results/people/?keywords={first_name}%20{last_name}'
    driver.get(search_url)
    time.sleep(5)

    try:
        connect_button = driver.find_element(By.XPATH, '//button[text()="Connect"]')
        connect_button.click()
    except:
        print(f"Connect button not found for {first_name} {last_name}. Skipping to the next person.")

main()
