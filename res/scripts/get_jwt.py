from selenium                       import webdriver
from selenium.webdriver.common.by   import By

import logging
import time

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_jwt(email: str, password: str) -> str:

    """
    Get the JWT token from the PixAI website.

    :param email: The email to login with.
    :param password: The password to login with.

    :return: The JWT token as a string.
    """

    # Start a new instance of Chrome web browser
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.minimize_window()

    # Open the URL in the browser
    browser.get('about:blank')
    browser.get('https://pixai.art/login?to=/generator/realtime/text')

    # Wait for a bit to let the page load
    time.sleep(2)

    # Click button with specific text
    nextbtn = browser.find_element(By.XPATH, '//button[contains(text(), "Mit E-Mail anmelden")]')
    nextbtn.click()

    # Wait for a bit to let the next page load
    time.sleep(1)

    # Find email input field by id and send keys
    email_input = browser.find_element(By.ID, "email-input")
    email_input.send_keys(f"{email}")
    logging.info("Sent email to input field.")
    #time.sleep(0.5)

    # Find password input field by id and send keys
    password_input = browser.find_element(By.ID, "password-input")
    password_input.send_keys(f"{password}")
    logging.info("Sent password to input field.")
    #time.sleep(0.5)

    # Find login button by id and click
    login_btn = browser.find_element(By.XPATH, '//button[contains(text(), "Anmelden")]')
    login_btn.click()
    logging.info("Clicked login button.")

    # Let the page load
    time.sleep(2)

    # Get local storage entry
    localstorage = browser.execute_script("return window.localStorage;")
    jwt: str = str(localstorage['https://api.pixai.art:token'])
    logging.info("Got JWT token. Terminating browser.")

    # Wait for some time before closing the browser
    browser.quit()

    return jwt