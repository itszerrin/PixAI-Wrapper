from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from time import sleep

# logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def claim_daily_credits(email: str, password: str) -> None:
    """
    Log into the PixAI website and claim the daily credits.

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

    # Wait for the "Log in with email" button to be clickable
    nextbtn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[contains(text(), "Log in with email")]'))
    )
    nextbtn.click()

    # Find email input field by id and send keys
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "email-input"))
    )
    email_input.send_keys(f"{email}")
    logging.info("Credits - Sent email to input field.")

    # Find password input field by id and send keys
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "password-input"))
    )
    password_input.send_keys(f"{password}")
    logging.info("Credits - Sent password to input field.")

    # Find login button by id and click
    login_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[contains(text(), "Login")]'))
    )
    login_btn.click()
    logging.info("Credits - Clicked login button.")

    # Click two buttons to get to the profile page with the claim button
    try:
        # get the last child of header element and click it
        profileIcon_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//header/*[last()]"))
        )
        profileIcon_btn.click()

        # click the span element with the text "Profile"
        profile_btn = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(), 'Profile')]"))
        )
        profile_btn.click()
    except:
        logging.info("Credits - An Error Occurred.")
        quit('An Error Occurred: Could not find profile icon button or profile button.')

    sleep(1)

    # finds the specific button that contains the text "Claim"/"Claimed"
    try:
        claim_btn = WebDriverWait(browser, 4).until(
            EC.presence_of_element_located(
                (By.XPATH, "//section//div//div[2]//div[2]//button"))
        )
        text = claim_btn.get_attribute("textContent").strip()
        if text == "Claimed":
            logging.info("Credits - Already claimed.")
            browser.quit()
            return
    except:
        logging.info("Credits - An Error Occurred.")
        quit('An Error Occurred: Could not find claim button.')

    # click the button that contains a span element with the text "Claim"
    claim_btn.click()
    sleep(1.5) # time to register the click
    logging.info("Credits - Clicked claim button.")

    # Close the browser
    browser.quit()
