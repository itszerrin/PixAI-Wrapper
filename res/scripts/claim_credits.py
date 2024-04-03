from selenium                       import webdriver
from selenium.webdriver.common.by   import By

import logging
import time

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def claim_daily_credits(id: str, email: str, password: str) -> None:

    """
    Log into the PixAI website and claim the daily credits.

    :param id: The user ID to claim the credits for.
    :param email: The email to login with.
    :param password: The password to login with.

    :return: None
    """

    # Start a new instance of Chrome web browser
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en-US")
    browser = webdriver.Chrome(options=options)
    browser.minimize_window()

    # Open the URL in the browser
    browser.get('about:blank')
    browser.get('https://pixai.art/login?to=/generator/realtime/text')

    # Wait for a bit to let the page load
    time.sleep(2)

    # Click button with specific text
    nextbtn = browser.find_element(By.XPATH, '//button[contains(text(), "Log in with email")]')
    nextbtn.click()

    # Wait for a bit to let the next page load
    time.sleep(1)

    # Find email input field by id and send keys
    email_input = browser.find_element(By.ID, "email-input")
    email_input.send_keys(f"{email}")
    logging.info("Credits - Sent email to input field.")
    #time.sleep(0.5)

    # Find password input field by id and send keys
    password_input = browser.find_element(By.ID, "password-input")
    password_input.send_keys(f"{password}")
    logging.info("Credits - Sent password to input field.")
    #time.sleep(0.5)

    # Find login button by id and click
    login_btn = browser.find_element(By.XPATH, '//button[contains(text(), "Login")]')
    login_btn.click()
    logging.info("Credits - Clicked login button.")

    # wait for a bit to let the page load
    time.sleep(2)

    # go to new site
    browser.get(f"https://pixai.art/@user-{id}/artworks")

    # wait for a bit to let the page load
    time.sleep(2)

    # find button with specific class
    try:    claim_btn = browser.find_element(By.XPATH, "//button[contains(span/text(), 'Claim')]")
    except: 
        
        # try finding claimed text instead
        try:    claim_btn = browser.find_element(By.XPATH, "//button[contains(span/text(), 'Claimed')]");    logging.info("Credits - Already claimed.");   return
        except:
            logging.info("Credits - An Error Occurred.")
            quit('An Error Occurred: Could not find "Claimed" or "Claim" button.')

    claim_btn.click()
    logging.info("Credits - Clicked claim button.")

    # Wait a second
    time.sleep(1)

    # Close the browser
    browser.quit()