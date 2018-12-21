from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import sys
import time
import random
import re


def chrome_me(url):
    try:
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--windows-size=1920*1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-proxy-server")

        chrome_driver = os.getcwd() + "/bin/chromedriver"
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
        driver.get(url)

    except Exception as request_error:
        print('there seems to be an issue with the url you are requesting.')
        print(request_error)
        sys.exit(1)

    return driver


def grab_em(company_name):
    linkedin_login = 'https://www.linkedin.com'
    user_id = '**********'
    user_password = '***************'

    driver = chrome_me(linkedin_login)
    time.sleep(random.uniform(3.5, 6.9))

    try:
        email_element = driver.find_element_by_class_name("login-email")
        pass_element = driver.find_element_by_class_name("login-password")
        submit_button = driver.find_element_by_id("login-submit")
        email_element.send_keys(user_id)
        pass_element.send_keys(user_password)
        print('I found them and added the passwords!')
        time.sleep(random.uniform(1.2, 4.1))
        print('submitting')
        submit_button.click()

    except NoSuchElementException as exception:
        print("we seem to not be able to find the elements. Please update class name of element")
        print(exception)

    print("we are in!")
    try:
        search_box = driver.find_element_by_xpath('''//*[@id="ember41"]/input''')
        search_box.send_keys('''"''' + company_name + '''"''')
        search_box.send_keys(Keys.RETURN)

    except NoSuchElementException as exception:
        print("we seem to be having trouble finding that element")
        print(exception)

    print('made it!')

    complete_img_list = []

    while True:
        try:
            time.sleep(10)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            page = driver.find_element_by_tag_name("html")
            page.send_keys(Keys.END)
            next_page = driver.find_element_by_class_name("next-text")
            time.sleep(random.uniform(3.1, 4.2))
            print(driver.current_url)
            page_source = driver.page_source

            soup = BeautifulSoup(page_source, 'html.parser')

            c4 = soup.find_all(src=re.compile("https://media.licdn.com/dms/image/C4"))
            c5 = soup.find_all(src=re.compile("https://media.licdn.com/dms/image/C5"))

            c4_src = [x['src'] for x in c4]
            c5_src = [y['src'] for y in c5]

            pg_img_urls = c4_src + c5_src
            for img_url in pg_img_urls:
                complete_img_list.append(img_url)
                # print(img_url)
            time.sleep(random.uniform(35.2, 48.1))
            next_page.click()
            continue
        except NoSuchElementException as exception:
            print('this looks to be the last page')
            page_source = driver.page_source

            soup = BeautifulSoup(page_source, 'html.parser')

            c4 = soup.find_all(src=re.compile("https://media.licdn.com/dms/image/C4"))
            c5 = soup.find_all(src=re.compile("https://media.licdn.com/dms/image/C5"))

            c4_src = [x['src'] for x in c4]
            c5_src = [y['src'] for y in c5]

            pg_img_urls = c4_src + c5_src
            for img_url in pg_img_urls:
                complete_img_list.append(img_url)
                print(img_url)
            break

    print(complete_img_list)
    for total_img in complete_img_list:
        if '100_100' in total_img:
            complete_img_list.remove(total_img)

    time.sleep(25.5)

    driver.close()
    driver.quit()
    return list(set(complete_img_list))


# completed_urls = grab_em('people data labs')
# print(completed_urls)
