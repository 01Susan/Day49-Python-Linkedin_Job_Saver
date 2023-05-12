import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait

# set the location of the Chrome webdriver
web_driver_location = r"D:\Downloads\chromedriver_win32\chromedriver.exe"
# create a service object with the web driver location
service = Service(web_driver_location)
# create a Chrome webdriver instance using the service
driver = webdriver.Chrome(service=service)
# navigate to the LinkedIn homepage
driver.get("https://www.linkedin.com/home")
# maximize the window
driver.maximize_window()

# load user login credentials from environment variables
load_dotenv()
email = os.getenv("LINKEDIN_ID")
password = os.getenv("PASSWORD")


def login():
    # locate the email input field on the login page and enter the user's email address
    email_section = driver.find_element(By.ID, 'session_key')
    email_section.send_keys(email)

    # locate the password input field on the login page and enter the user's password
    password_section = driver.find_element(By.ID, "session_password")
    password_section.send_keys(password)

    # locate and click the "Sign in" button on the login page
    sign_up = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    sign_up.click()

    # wait for the search bar to appear on the home page, indicating a successful login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.search-global-typeahead__input")))


def search_global():
    # locate the search input field on the home page and enter the desired search query
    global_search = driver.find_element(by=By.CSS_SELECTOR, value="input.search-global-typeahead__input")
    global_search.send_keys("frontend intern")
    global_search.send_keys(Keys.ENTER)

    # wait for the search results to appear
    # note: this can be made more robust by waiting for a specific element to appear in the search results
    # instead of just waiting for any element to appear
    # e.g. WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.search-result__info")))


def navigate():
    # locate the "Easy Apply" filter link in the search results and click it
    easy_apply = driver.find_elements(by=By.CSS_SELECTOR, value='ul.reusable-search__entity-cluster--quick-filter-action-container li a')
    for apply in easy_apply[1:2]:
        apply.click()

    # wait for the filtered search results to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.job-card-container--clickable")))


def job_list():
    # locate all the job cards in the search results and iterate through them
    jobs_list = driver.find_elements(by=By.CSS_SELECTOR, value="div.job-card-container--clickable")
    job_no = len(jobs_list)
    for job in range(job_no):
        # click on the job card to view the job details
        jobs_list[job].click()

        # locate the "Save" button on the job details page and click it
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "jobs-save-button"))).click()

    # close the browser window
    driver.quit()


# call the functions in sequence to automate the job search and saving process
login()
search_global()
time.sleep(5)
navigate()
time.sleep(5)
job_list()
