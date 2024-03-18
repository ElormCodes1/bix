import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import datetime
import requests
import json
import random
import os
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

opt = webdriver.ChromeOptions()
opt.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
opt.add_experimental_option("detach", True)
# opt.add_argument("--headless")

driver = webdriver.Chrome(options=opt)

wait = WebDriverWait(driver, 10)

break_number = 0

link = "https://www.google.com/maps/"

actions = ActionChains(driver)

# url = "https://chromewebstore.google.com/detail/quillbot-ai-writing-and-g/iidnbdjijdkbmajdffnidomddglmieko"
driver.get(link)
# driver.maximize_window()

input_element = driver.find_element(By.CSS_SELECTOR, "input.searchboxinput")

input_element.send_keys("Dental clinics in Dubai")

input_element.send_keys(Keys.ENTER)

time.sleep(5)

# rating_button_check = driver.find_elements(By.CSS_SELECTOR, "button.e2moi ")

rating_button = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button.e2moi "))
)
time.sleep(10)
rating_button.click()

rating_button.click()

starbutton = driver.find_element(By.CSS_SELECTOR, "div[data-index='6']")

time.sleep(5)

starbutton.click()

time.sleep(5)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# time.sleep(50)

contentdiv = driver.find_element(By.CSS_SELECTOR, "div.Ntshyc ")

body = driver.find_element(By.CSS_SELECTOR, "div.e07Vkf.kA9KIf")

driver.execute_script("arguments[0].focus();", body)

contentdiv.click()

# driver.execute_script(f"arguments[0].scrollTop = arguments[0].scrollTop + 100;", body)
while True:
    actions.send_keys(Keys.END).perform()
    time.sleep(random.randint(1, 10))
    try:
        last_item = driver.find_element(By.CSS_SELECTOR, "span.HlvSq")
        print(last_item.text)
        if last_item:
            break
    except:
        continue

# all_items = driver.find_elements(By.CSS_SELECTOR, "div.lI9IFe ")
# print(len(all_items))

# all_items = driver.find_elements(By.CSS_SELECTOR, "a.hfpxzc")

all_items = driver.find_elements(By.CSS_SELECTOR, "div.Nv2PK.tH5CWc.THOPZb ")
other_items = driver.find_elements(By.CSS_SELECTOR, "div.Nv2PK.Q2HXcd.THOPZb ")
all_items.extend(other_items)
print(f"total items: {len(all_items)}")
if len(all_items) == 0:
    try:
        all_items = driver.find_elements(By.CSS_SELECTOR, "div.Nv2PK.THOPZb.CpccDe ")
        print(f"total items: {len(all_items)}")
    except:
        print("No items found")
# leads = []
# print(len(leads))

for item in all_items:
    # driver.execute_script("arguments[0].scrollIntoView();", item)
    # test = item.find_elements(By.CSS_SELECTOR, "div.etWJQ.jym1ob.kdfrQc.bWQG4d ")
    # print("this is the length of test", len(test))
    # if len(test) == 1:
    #     name = item.find_element(By.CSS_SELECTOR, "div.qBF1Pd.fontHeadlineSmall ").text
    #     try:
    #         telephone = item.find_element(By.CSS_SELECTOR, "span.UsdlK").text
    #     except:
    #         telephone = "NaN"
    #     data = {
    #         "name": name,
    #         "telephone": telephone,
    #     }
    #     print(data)
    #     leads.append(data)
    #     with open("montdent.txt", "a") as f:
    #         f.write(telephone + "\n")

    # else:
    #     continue
    try:
        telephone = item.find_element(By.CSS_SELECTOR, "span.UsdlK").text
    except:
        telephone = None
    try:
        website = item.find_element(By.CSS_SELECTOR, "a.lcr4fd.S9kvJb ").get_attribute(
            "href"
        )
    except:
        website = False
    try:
        reviews = item.find_element(By.CSS_SELECTOR, "span.e4rVHe.fontBodyMedium").text
        reviews = reviews[reviews.index("(") + 1 : reviews.index(")")].replace(",", "")
    except:
        reviews = None

    item = item.find_element(By.CSS_SELECTOR, "a.hfpxzc")
    driver.execute_script("arguments[0].scrollIntoView();", item)
    time.sleep(1)
    try:
        item.click()
    except:
        print("Exception occurred, skipping")
        continue

    # item = item.find_element(By.CSS_SELECTOR, "div.lI9IFe ")
    time.sleep(5)
    try:
        business_name = driver.find_element(By.CSS_SELECTOR, "h1.DUwDvf.lfPIob").text
    except:
        business_name = None
    try:
        average_star = driver.find_element(
            By.CSS_SELECTOR, "div.F7nice  span span"
        ).text
    except:
        average_star = None
    # reviews = driver.find_elements(By.CSS_SELECTOR, "div.F7nice  span span")
    # reviews = reviews[1].text
    if website == False:
        try:
            website = driver.find_element(By.CSS_SELECTOR, "a.CsEnBe").get_attribute(
                "href"
            )
        except:
            website = None
    business_type = driver.find_element(By.CSS_SELECTOR, "button.DkEaL ").text
    address = driver.find_element(
        By.CSS_SELECTOR, "div.Io6YTe.fontBodyMedium.kR99db "
    ).text
    # website = driver.find_element(By.CSS_SELECTOR, "a.CsEnBe").get_attribute("href")
    # telephone = driver.find_elements(
    #     By.CSS_SELECTOR, "div.Io6YTe.fontBodyMedium.kR99db "
    # )
    business_details = {
        "business_name": business_name,
        "average_star": average_star,
        "reviews": reviews,
        "business_type": business_type,
        "address": address,
        "telephone": telephone,
        "website": website,
    }
    with open("dubaidentist.json", "a") as f:
        json.dump(business_details, f)
        f.write("\n")

    print(business_details)


# print(len(leads))


# while True:
# driver.execute_script("arguments[0].focus();", contentdiv)
# pyautogui.scroll(-100)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# driver.execute_script(
#     f"arguments[0].scrollTop = arguments[0].scrollTop + 100;", body
# )
# body.send_keys(Keys.ARROW_DOWN)
