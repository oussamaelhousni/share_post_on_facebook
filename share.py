from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options

import time
from dotenv import dotenv_values

config = dotenv_values(".env")

# Set Chrome options to disable notifications
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.jumia.ma/ordinateurs-accessoires-informatique/"

# Constants
EMAIL = config["EMAIL"]
PASSWORD = config["PASSWORD"]

FACEBOOK_LOGIN_URL = 'https://web.facebook.com/'
FACEBOOK_URL = "https://web.facebook.com/xxx.xxxx.12" # link to your profile
ADD_PHOTO_XPATH = 'div > div:nth-child(1) > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x78zum5.xdt5ytf.x1t2pt76 > div > div > div.x6s0dn4.x78zum5.xdt5ytf.x193iq5w > div.x9f619.x193iq5w.x1talbiv.x1sltb1f.x3fxtfs.x1swvt13.x1pi30zi.xw7yly9 > div > div.x9f619.x1n2onr6.x1ja2u2z.xeuugli.xs83m0k.x1xmf6yo.x1emribx.x1e56ztr.x1i64zmx.xjl7jj.x19h7ccj.xu9j1y6.x7ep2pv > div:nth-child(1) > div > div > div > div > div.xqmpxtq.x13fuv20.x178xt8z.x78zum5.x1a02dak.x1vqgdyp.x1l1ennw.x14vqqas.x6ikm8r.x10wlt62.x1y1aw1k'
                    
UPLOAD_INPUT_XPATH = 'div > div:nth-child(1) > div > div:nth-child(5) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > form > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x10l6tqk.x17qophe.x13vifvy.x1hc1fzr.x71s49j > div > div > div > div.xb57i2i.x1q594ok.x5lxg6s.x6ikm8r.x1ja2u2z.x1pq812k.x1rohswg.xfk6m8.x1yqm8si.xjx87ck.xx8ngbg.xwo3gff.x1n2onr6.x1oyok0e.x1odjw0f.x1e4zzel.x78zum5.xdt5ytf.x1iyjqo2 > div.x78zum5.xdt5ytf.x1iyjqo2.x1n2onr6 > div.x1sxyh0.xurb0ha > div > div.x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x193iq5w.x1l7klhg.x1iyjqo2.xs83m0k.x2lwn1j.x1y1aw1k.xwib8y2 > div > div:nth-child(1) > input'
POST_BTN_XPATH = 'div > div:nth-child(1) > div > div:nth-child(5) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > form > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x10l6tqk.x17qophe.x13vifvy.x1hc1fzr.x71s49j > div > div > div > div.x1l90r2v.xyamay9.x1n2onr6 > div.x6s0dn4.x9f619.x78zum5.x1qughib.x1pi30zi.x1swvt13.xyamay9.xh8yej3 > div'
TEXTAREA = "div > div:nth-child(1) > div > div:nth-child(5) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > form > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x10l6tqk.x17qophe.x13vifvy.x1hc1fzr.x71s49j > div > div > div > div.xb57i2i.x1q594ok.x5lxg6s.x6ikm8r.x1ja2u2z.x1pq812k.x1rohswg.xfk6m8.x1yqm8si.xjx87ck.xx8ngbg.xwo3gff.x1n2onr6.x1oyok0e.x1odjw0f.x1e4zzel.x78zum5.xdt5ytf.x1iyjqo2 > div.x78zum5.xdt5ytf.x1iyjqo2.x1n2onr6 > div.x1ed109x.x1iyjqo2.x5yr21d.x1n2onr6.xh8yej3 > div.x9f619.x1iyjqo2.xg7h5cd.x1swvt13.x1n2onr6.xh8yej3.x1ja2u2z.x11eofan > div > div > div.xzsf02u.x1a2a7pz.x1n2onr6.x14wi4xw.x9f619.x1lliihq.x5yr21d.xh8yej3.notranslate"
INPUT_PARAGRAPH = "div > div:nth-child(1) > div > div:nth-child(5) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > form > div > div.x9f619.x1ja2u2z.x1k90msu.x6o7n8i.x1qfuztq.x10l6tqk.x17qophe.x13vifvy.x1hc1fzr.x71s49j > div > div > div > div.xb57i2i.x1q594ok.x5lxg6s.x6ikm8r.x1ja2u2z.x1pq812k.x1rohswg.xfk6m8.x1yqm8si.xjx87ck.xx8ngbg.xwo3gff.x1n2onr6.x1oyok0e.x1odjw0f.x1e4zzel.x78zum5.xdt5ytf.x1iyjqo2 > div.x78zum5.xdt5ytf.x1iyjqo2.x1n2onr6 > div.x1ed109x.x1iyjqo2.x5yr21d.x1n2onr6.xh8yej3 > div.x9f619.x1iyjqo2.xg7h5cd.x1swvt13.x1n2onr6.xh8yej3.x1ja2u2z.x11eofan > div > div > div > p"

def wait_and_find_element(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        print(f"Timeout waiting for element {value}")
        return None

def login_to_facebook():
    driver.get(FACEBOOK_LOGIN_URL)
    email_input = wait_and_find_element(driver, By.XPATH, '//*[@id="email"]')
    password_input = wait_and_find_element(driver, By.XPATH, '//*[@id="pass"]')
    submit_btn = wait_and_find_element(driver, By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')

    if email_input and password_input and submit_btn:
        email_input.send_keys(EMAIL)
        password_input.send_keys(PASSWORD)
        submit_btn.click()
        print("Logged in successfully")
        return True
    else:
        print("Login elements not found")
        return False

def upload_photo(img="C:\\Users\\oussa\\OneDrive\Desktop\\hard\\IMG-20230502-WA0019-01.jpeg",text="automated by selenium"):
    driver.get(FACEBOOK_URL)
    print("My Facebook page")
    add_btn = wait_and_find_element(driver, By.CSS_SELECTOR, ADD_PHOTO_XPATH)
    if add_btn:
        add_btn.click()
        upload = wait_and_find_element(driver, By.CSS_SELECTOR, UPLOAD_INPUT_XPATH,15)
        post_btn = wait_and_find_element(driver, By.CSS_SELECTOR, POST_BTN_XPATH)
        textarea = wait_and_find_element(driver,By.CSS_SELECTOR,TEXTAREA)
        input_paragraph = wait_and_find_element(driver,By.CSS_SELECTOR,INPUT_PARAGRAPH)
        if upload and post_btn and textarea and input_paragraph:
            upload.send_keys(img)
            time.sleep(3)
            textarea.click()
            input_paragraph.send_keys(text)
            post_btn.click()
            time.sleep(10)
            driver.close()
            print("Photo uploaded successfully")
            return True
        else:
            print("Upload elements not found")
            return False
    else:
        print("Add button not found")
        return False

def share_on_facebook():
    try:
        if login_to_facebook():
            time.sleep(5)
            upload_photo()
            time.sleep(30)
    except NoSuchElementException as e:
        print(f"Exception: {str(e)}")

# Call the main function
share_on_facebook()
