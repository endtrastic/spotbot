from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import undetected_chromedriver as uc
import time
import random
import sys
from dotenv import load_dotenv
import os
 

def im_human():
    time.sleep(random.uniform(1.0, 6.0))

def mains():
    im_human()
    driver = uc.Chrome(headless=True, use_subprocess=True)
    time.sleep(5)
    try:
        if len(sys.argv) < 2:
            print("Error: No playlist ID provided.")
            sys.exit(1)

        song_url = sys.argv[1]

        print(f"Download the song with the link below >_<")



        driver.get('https://spotidown.app/')

        im_human()
        time.sleep(5)

        try: 
            Try_to_consent = WebDriverWait(driver, 7).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 
                    'body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-do-not-consent.fc-secondary-button'))
            )

            Try_to_consent.click()
        except TimeoutException:
            pass

        im_human()

        Url_textbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="url"]')))

        im_human()

        Url_textbox.send_keys(song_url)


        Download_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#send'))
        )

        Download_button.click()

        im_human()

        Download_url = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="download-section"]/div/div/div[1]/div[3]/div[1]/a'))
        )

        buttons_url = Download_url.get_attribute('href')
        print(buttons_url)


    finally:
        driver.quit()


if __name__ == "__main__":
    try:
        mains()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("Error occurred during execution", file=sys.stderr)