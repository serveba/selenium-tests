# To install the Python client library:
# pip install -U selenium

# Import the Selenium 2 namespace (aka "webdriver")
from selenium import webdriver
import getpass 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from os import listdir
from os.path import join, isdir



def retrieve_ff_profile():
    # Firefox profile, for loading user certificates in MAC
    user = getpass.getuser()
    fp_path = "/Users/" + user + "/Library/Application Support/Firefox/Profiles/"
    only_folders = [f for f in listdir(fp_path) if isdir(join(fp_path, f))]

    for folder in only_folders:
        if ".default" in folder:
            fp_path = fp_path + folder
            break    
    print fp_path
    return fp_path

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True

fp = webdriver.FirefoxProfile(retrieve_ff_profile())
browser = webdriver.Firefox(fp)

# Go to URL
browser.get(
    'https://www.google.com')

delay = 3  # seconds
try:
    myElem = WebDriverWait(browser, delay).until(
        EC.presence_of_element_located((By.ID, 'lst-ib')))
    print "Page is ready!"
except TimeoutException:
    print browser.current_url
    print "Page Load took more than " + str(delay) + " seconds..."

input_text = browser.find_element_by_id('lst-ib')
input_text.clear()
input_text.send_keys("selenium")

feeling_lucky_btn = browser.find_element_by_name('btnI')
feeling_lucky_btn.click()

# browser.quit()
