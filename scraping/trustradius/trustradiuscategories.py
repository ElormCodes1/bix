from calendar import c
from nis import cat
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
import datetime
import json
import random
import psycopg2
import concurrent.futures

# from proxies import PROXY_LIST
from bs4 import BeautifulSoup
import re
import os
from dotenv import load_dotenv

load_dotenv()

PROXY_USERNAME = os.getenv("PROXY_USERNAME")
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")

PROXY_LIST = [
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.238.20.59:5681",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.72.54.208:8632",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.94.45.58:7061",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@103.47.52.10:8052",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@154.194.8.232:5763",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.61.124.241:6570",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@109.207.130.7:8014",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@157.52.145.59:5668",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@185.230.46.65:5714",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@91.246.194.37:6550",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@93.120.32.196:9380",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@161.123.33.234:6257",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@37.35.40.199:8289",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.144.3.112:6191",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.148.5.9:6020",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@154.92.123.54:5392",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@198.46.137.84:6288",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.136.173.78:7668",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.238.38.179:6447",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@138.128.159.21:6512",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@194.33.29.181:7765",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@23.250.101.218:8270",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@5.183.35.57:5327",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@23.229.101.174:8698",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@64.137.42.20:5065",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.144.78.214:9259",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@154.95.1.112:6634",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@194.39.34.163:6175",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@154.85.100.64:5105",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@173.211.30.152:6586",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@154.30.251.136:5277",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.239.107.34:5686",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@141.98.161.78:7775",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.56.173.229:6212",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.152.200.16:9562",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.192.138.17:6659",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@184.174.44.7:6433",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@103.53.216.134:5218",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@198.154.89.174:6265",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.56.175.244:5918",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.192.145.62:5404",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.61.116.135:6813",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.61.118.108:5805",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.61.125.134:6145",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.140.13.134:9147",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.232.209.161:6119",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@194.33.61.138:8721",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@198.105.111.153:6831",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.152.202.195:9200",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@194.35.123.205:7625",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@192.210.132.8:5978",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@192.156.217.90:7164",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.127.248.75:5076",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@198.154.89.80:6171",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@23.247.7.196:5869",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@93.120.32.159:9343",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@173.211.8.193:6305",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@198.46.246.40:6664",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.56.175.26:5700",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.233.13.252:6247",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@109.196.160.31:5777",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@5.154.253.33:8291",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.223.223.6:6591",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@107.152.177.174:6194",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@141.98.133.10:7386",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.239.80.91:5669",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.89.105.231:6904",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@107.181.154.144:5822",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.41.177.104:5754",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@107.172.156.36:5684",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@192.166.153.86:8161",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@157.52.233.185:5812",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@5.154.253.254:8512",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.87.243.228:6230",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@185.30.232.179:6058",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@172.245.158.90:6043",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@198.46.137.181:6385",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@107.152.197.33:8055",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.61.125.9:6020",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.148.5.174:6185",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.127.250.63:5672",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@154.16.243.136:6280",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@185.136.204.229:5590",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@64.43.89.10:6269",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@176.116.230.30:7116",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.94.46.69:6083",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@107.152.177.63:6083",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@67.227.110.205:6763",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.238.37.131:6688",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@172.245.158.75:6028",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.72.55.180:7217",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@2.56.174.247:5553",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.137.60.124:6652",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@103.75.228.71:6150",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.239.106.224:5869",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@161.123.66.67:6840",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.56.173.122:6105",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.238.50.134:6680",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@194.33.29.88:7672",
    f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@64.137.73.191:5279",
]

usable_proxies = PROXY_LIST

dead_proxies = []

try:
    os.remove("getappcategories.json")
except:
    pass


chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()
options.add_argument("disable-cookies")
options.add_argument("disable-extensions")
options.add_argument("disable-gpu")
options.add_argument("disable-infobars")
options.add_argument("disable-notifications")
options.add_argument("disable-popup-blocking")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
# options.add_argument("--remote-debugging-port=9222")
options.add_argument("--remote-debugging-pipe")
# options.add_experimental_option("detach", True)
options.add_argument("--headless")

curr_proxy_num = 0

webdriver.DesiredCapabilities.CHROME["proxy"] = {
    "httpProxy": usable_proxies[curr_proxy_num],
    "ftpProxy": usable_proxies[curr_proxy_num],
    "sslProxy": usable_proxies[curr_proxy_num],
    "proxyType": "MANUAL",
}

all_cat_links = []

SCRAPING_DATE = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

driver = webdriver.Chrome(options=options)

url = "https://www.trustradius.com/categories"

driver.get(url)

page_content = driver.page_source

soup = BeautifulSoup(page_content, "html.parser")

cat_links = soup.find_all("a", class_="btn btn-link")

cat_links = [f"https://trustradius.com{link['href']}" for link in cat_links]

for link in cat_links:
    print(link)
    driver.get(link)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, "html.parser")
    mcat_links = soup.find_all("a")
    mcat_links = [link for link in mcat_links if "#products" in link["href"]]
    mcat_links = [f"https://trustradius.com{link['href']}" for link in mcat_links]
    # print(mcat_links)
    all_cat_links.extend(mcat_links)
driver.close()

# seen = set()

# print(len(all_cat_links))

# all_cat_links = [x for x in all_cat_links if x not in seen and not seen.add(x)]

print(f"total cats {len(all_cat_links)}")


# def process_link(link, proxy_index):
#     global curr_proxy_num

#     try:
#         response = requests.get(link, proxies={"http": usable_proxies[proxy_index]})
#     except Exception as e:
#         print(f"Error fetching {link}: {e}")
#         if len(usable_proxies) == 0:
#             usable_proxies.append(dead_proxies)
#         curr_proxy_num = 0
#         # return
#         try:
#             response = requests.get(
#                 link, proxies={"http": usable_proxies[curr_proxy_num]}
#             )
#         except Exception as e:
#             print(f"Error fetching {link} again: {e}")
#             return

#     page_content = response.text
#     soup = BeautifulSoup(page_content, "html.parser")
#     cat_data = soup.find_all("script", type="application/ld+json")

#     try:
#         jdata = json.loads(cat_data[0].text)
#     except Exception as e:
#         print(f"Error parsing JSON for {link}: {e}")
#         # print(jdata)
#         usable_proxies.remove(usable_proxies[curr_proxy_num])
#         dead_proxies.append(usable_proxies[curr_proxy_num])
#         time.sleep(15)
#         return

#     try:
#         name = jdata[1]["name"]
#     except Exception as e:
#         print(f"Error extracting name for {link}: {e}")
#         return

#     if "Best " in name:
#         name = name.split("Best ")[1]

#     total_apps = jdata[1]["numberOfItems"]
#     category_url = link
#     scraped_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     full_data = {
#         "name": name,
#         "total_apps": total_apps,
#         "category_url": category_url,
#         "scraped_time": scraped_time,
#     }

#     print(full_data)

#     with open("trustradiuscategories.json", "a") as f:
#         f.write(json.dumps(full_data) + "\n")


# max_workers = 5
# num_links = len(all_cat_links)
# num_batches = num_links + max_workers - 1


# # Set up the ThreadPoolExecutor with a maximum of 5 concurrent threads
# with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
#     for batch in range(num_batches):
#         start_idx = batch * max_workers
#         end_idx = min((batch + 1) * max_workers, num_links)

#         # Generate proxy indexes for this batch
#         proxy_indexes = range(start_idx, end_idx)

#         # Submit tasks for this batch
#         futures = []
#         for link, proxy_index in zip(all_cat_links[start_idx:end_idx], proxy_indexes):
#             future = executor.submit(process_link, link, proxy_index)
#             futures.append(future)

#         # Wait for the tasks in this batch to complete
#         for future in concurrent.futures.as_completed(futures):
#             future.result()

page_content = None

for link in all_cat_links:
    print(link)
    curr_proxy_num += 1
    if len(usable_proxies) == 0:
        usable_proxies.append(dead_proxies)
    print(curr_proxy_num)
    if curr_proxy_num > len(usable_proxies) - 1:
        curr_proxy_num = 0
    try:
        response = requests.get(link, proxies={"http": usable_proxies[curr_proxy_num]})
        if response.status_code != 200:
            print(f"403 error for {link}")
            curr_proxy_num += 1
            if len(usable_proxies) == 0:
                usable_proxies.append(dead_proxies)
            if curr_proxy_num > len(usable_proxies) - 1:
                curr_proxy_num = 0
            print("trying again")
            # response = requests.get(
            #     link, proxies={"http": usable_proxies[curr_proxy_num]}
            # )
            driver = webdriver.Chrome(options=options)
            driver.get(link)
            page_content = driver.page_source
    except:
        curr_proxy_num += 1
        if len(usable_proxies) == 0:
            usable_proxies.append(dead_proxies)
        if curr_proxy_num > len(usable_proxies) - 1:
            curr_proxy_num = 0
        # response = requests.get(link, proxies={"http": usable_proxies[curr_proxy_num]})
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        page_content = driver.page_source
        driver.close()
        # continue
    print(response.status_code)
    # driver = webdriver.Chrome(options=options)
    # driver.get(link)
    if page_content is None:
        page_content = response.text
    # page_content = driver.page_source
    soup = BeautifulSoup(page_content, "html.parser")
    cat_data = soup.find_all("script", type="application/ld+json")

    # len(cat_data)
    try:
        jdata = json.loads(cat_data[0].text)
    except:
        print(cat_data)
        usable_proxies.remove(usable_proxies[curr_proxy_num])
        print(f"total usable proxies: {len(usable_proxies)}")
        dead_proxies.append(usable_proxies[curr_proxy_num])
        print(f"total dead proxies: {len(dead_proxies)}")
        page_content = None
        continue
    # print(jdata)
    try:
        name = jdata[1]["name"]
    except Exception:
        print("did not find the data")
        cat_data = soup.find_all("script", type="text/javascript")
        print("getting other json text")
        data = cat_data[5].text
        print("getting it from the list")
        jdata = data.replace("window.__INITIAL_DATA__ = ", "")
        print("removing the first part")
        jdata = jdata.split(
            "//- script adding redux store data from server to window so we can access it client side",
            1,
        )[0]
        print("removing the last part")
        jdata = json.loads(jdata)
        # with open("oneapp.json", "w") as f:
        #     f.write(json.dumps(jdata))
        print("loading the json")
        try:
            name = jdata["structuredData"][1]["name"]
        except Exception:
            print("no apps found")
            page_content = None
            continue
        print("getting the name")
        if "Best " in name:
            name = name.split("Best ")[1]
        print("splitting the name")
        total_apps = jdata["structuredData"][1]["numberOfItems"]
        print("getting the total apps")
        category_url = link
        print("getting the category url")
        scraped_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("getting the scraped time")
        full_data = {
            "name": name,
            "total_apps": total_apps,
            "category_url": category_url,
            "scraped_time": scraped_time,
        }
        print(full_data)
        with open("trustradiuscategories.json", "a") as f:
            f.write(json.dumps(full_data) + "\n")
        print("writing to file")
        page_content = None
        continue
    if "Best " in name:
        name = name.split("Best ")[1]
    total_apps = jdata[1]["numberOfItems"]
    category_url = link
    scraped_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_data = {
        "category_name": name,
        "total_apps": total_apps,
        "category_url": category_url,
        "scraped_time": scraped_time,
    }
    print(full_data)
    with open("trustradiuscategories.json", "a") as f:
        f.write(json.dumps(full_data) + "\n")
    # driver.close()
    if curr_proxy_num == len(usable_proxies):
        curr_proxy_num = 0
    page_content = None
# webdriver.DesiredCapabilities.CHROME["proxy"] = {
#     "httpProxy": PROXY_LIST[curr_proxy_num],
#     "ftpProxy": PROXY_LIST[curr_proxy_num],
#     "sslProxy": PROXY_LIST[curr_proxy_num],
#     "proxyType": "MANUAL",
# }

with psycopg2.connect(
    database="market_data",
    user="elorm",
    password="elorm",
    host="localhost",
    port="5432",
) as conn:
    with conn.cursor() as cursor:
        with open("trustradiuscategories.json", "r") as f:
            for line in f:
                data = json.loads(line)
                cursor.execute(
                    """insert into trustradius_categories(name, total_apps, url, scraped_time) values
                                    (%s, %s, %s, %s)""",
                    (
                        data["category_name"],
                        data["total_apps"],
                        data["category_url"],
                        data["scraped_time"],
                    ),
                )
        # Commit the insert
        conn.commit()

print("Data inserted successfully!")

os.remove("trustradiuscategories.json")

print("Data file removed successfully!")
