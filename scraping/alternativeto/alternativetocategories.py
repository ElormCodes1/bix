# import json
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import chromedriver_autoinstaller
# import datetime
# import random
# import os
# from dotenv import load_dotenv
# import psycopg2
# import os
# from bs4 import BeautifulSoup

# load_dotenv()

# PROXY_USERNAME = os.getenv("PROXY_USERNAME")
# PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")

# PROXY_LIST = [
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.238.20.59:5681",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.72.54.208:8632",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.94.45.58:7061",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@103.47.52.10:8052",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@154.194.8.232:5763",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.61.124.241:6570",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@109.207.130.7:8014",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@157.52.145.59:5668",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@185.230.46.65:5714",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@91.246.194.37:6550",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@93.120.32.196:9380",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@161.123.33.234:6257",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@37.35.40.199:8289",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.144.3.112:6191",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.148.5.9:6020",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@154.92.123.54:5392",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@198.46.137.84:6288",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.136.173.78:7668",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.238.38.179:6447",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@138.128.159.21:6512",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@194.33.29.181:7765",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@23.250.101.218:8270",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@5.183.35.57:5327",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@23.229.101.174:8698",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@64.137.42.20:5065",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.144.78.214:9259",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@154.95.1.112:6634",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@194.39.34.163:6175",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@154.85.100.64:5105",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@173.211.30.152:6586",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@154.30.251.136:5277",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.239.107.34:5686",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@141.98.161.78:7775",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.56.173.229:6212",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.152.200.16:9562",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.192.138.17:6659",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@184.174.44.7:6433",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@103.53.216.134:5218",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@198.154.89.174:6265",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.56.175.244:5918",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.192.145.62:5404",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.61.116.135:6813",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.61.118.108:5805",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.61.125.134:6145",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.140.13.134:9147",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.232.209.161:6119",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@194.33.61.138:8721",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@198.105.111.153:6831",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.152.202.195:9200",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@194.35.123.205:7625",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@192.210.132.8:5978",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@192.156.217.90:7164",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.127.248.75:5076",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@198.154.89.80:6171",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@23.247.7.196:5869",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@93.120.32.159:9343",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@173.211.8.193:6305",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@198.46.246.40:6664",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.56.175.26:5700",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.233.13.252:6247",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@109.196.160.31:5777",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@5.154.253.33:8291",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.223.223.6:6591",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@107.152.177.174:6194",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@141.98.133.10:7386",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.239.80.91:5669",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.89.105.231:6904",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@107.181.154.144:5822",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.41.177.104:5754",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@107.172.156.36:5684",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@192.166.153.86:8161",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@157.52.233.185:5812",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@5.154.253.254:8512",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.87.243.228:6230",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@185.30.232.179:6058",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@172.245.158.90:6043",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@198.46.137.181:6385",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@107.152.197.33:8055",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.61.125.9:6020",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.148.5.174:6185",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.127.250.63:5672",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@154.16.243.136:6280",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@185.136.204.229:5590",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@64.43.89.10:6269",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@176.116.230.30:7116",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.94.46.69:6083",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@107.152.177.63:6083",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@67.227.110.205:6763",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.238.37.131:6688",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@172.245.158.75:6028",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.72.55.180:7217",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@2.56.174.247:5553",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.137.60.124:6652",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@103.75.228.71:6150",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.239.106.224:5869",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@161.123.66.67:6840",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@45.56.173.122:6105",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@104.238.50.134:6680",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@194.33.29.88:7672",
#     f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@64.137.73.191:5279",
# ]


# chromedriver_autoinstaller.install()

# options = webdriver.ChromeOptions()
# options.add_argument("disable-cookies")
# options.add_argument("disable-extensions")
# options.add_argument("disable-gpu")
# options.add_argument("disable-infobars")
# options.add_argument("disable-notifications")
# options.add_argument("disable-popup-blocking")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# )
# options.add_argument("--remote-debugging-pipe")
# # options.add_experimental_option("detach", True)
# options.add_argument("--headless")

# webdriver.DesiredCapabilities.CHROME["proxy"] = {
#     "httpProxy": random.choice(PROXY_LIST),
#     "ftpProxy": random.choice(PROXY_LIST),
#     "sslProxy": random.choice(PROXY_LIST),
#     "proxyType": "MANUAL",
# }

# driver = webdriver.Chrome(options=options)

# url = "https://alternativeto.net/browse/all/"

# driver.get(url)

# page_content = driver.page_source

# soup = BeautifulSoup(page_content, "html.parser")

# script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
# if script_tag:
#     content = script_tag.string.strip()
# else:
#     content = None
# json_content = json.loads(content)
# request_id = json_content["buildId"]
# print(request_id)

# cat_links_link = f"https://alternativeto.net/_next/data/{request_id}/browse/all.json"

# app_list_url = "https://alternativeto.net/_next/data/AYOFDKXQed5cMq4Zec9cA/category/ai-tools/all.json?p=1"

# app_url = "https://alternativeto.net/_next/data/AYOFDKXQed5cMq4Zec9cA/software/stable-diffusion-web-ui/about.json?urlName=stable-diffusion-web-ui"

# page_num = 2

# curr_proxy = 0

# driver = webdriver.Chrome(options=options)
# driver.get(cat_links_link)

# json_data = driver.find_element(By.CSS_SELECTOR, "pre").get_attribute("innerText")
# driver.close()

# json_data = json.loads(json_data)

# all_apps_links = []

# for data_node in json_data["pageProps"]["allCategories"]["items"]:
#     if curr_proxy == len(PROXY_LIST):
#         curr_proxy = 0
#     webdriver.DesiredCapabilities.CHROME["proxy"] = {
#         "httpProxy": PROXY_LIST[curr_proxy],
#         "ftpProxy": PROXY_LIST[curr_proxy],
#         "sslProxy": PROXY_LIST[curr_proxy],
#         "proxyType": "MANUAL",
#     }
#     curr_proxy += 1
#     print(data_node["urlName"])
#     driver = webdriver.Chrome(options=options)
#     driver.get(
#         f"https://alternativeto.net/_next/data/{request_id}/category/{data_node['urlName']}/all.json"
#     )
#     try:
#         json_data_0 = driver.find_element(By.CSS_SELECTOR, "pre").get_attribute(
#             "innerText"
#         )
#     except:
#         continue
#     driver.close()
#     json_data_0 = json.loads(json_data_0)
#     name = json_data_0["pageProps"]["meta"]["h1Title"]
#     description = json_data_0["pageProps"]["meta"]["pageDescription"]
#     total_apps = json_data_0["pageProps"]["pagingMeta"]["totalCount"]
#     category_url = f"https://alternativeto.net/category/{data_node['urlName']}/all/"
#     SCRAPING_DATE = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     full_data = {
#         "category_name": name,
#         "category_description": description,
#         "total_apps_in_category": total_apps,
#         "category_url": category_url,
#         "scraped_time": SCRAPING_DATE,
#     }

#     print(full_data)
#     with open("alttocategoriesdata.json", "a") as f:
#         f.write(json.dumps(full_data) + "\n")

import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import datetime
import random
import os
from dotenv import load_dotenv
import psycopg2
import os
from bs4 import BeautifulSoup
import ast

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
try:
    os.remove("alttocategoriesdata.json")
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
options.add_argument("--remote-debugging-pipe")
# options.add_experimental_option("detach", True)
options.add_argument("--headless")

webdriver.DesiredCapabilities.CHROME["proxy"] = {
    "httpProxy": random.choice(PROXY_LIST),
    "ftpProxy": random.choice(PROXY_LIST),
    "sslProxy": random.choice(PROXY_LIST),
    "proxyType": "MANUAL",
}

driver = webdriver.Chrome(options=options)

url = "https://alternativeto.net/browse/all/"

driver.get(url)

page_content = driver.page_source

soup = BeautifulSoup(page_content, "html.parser")

script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
if script_tag:
    content = script_tag.string.strip()
else:
    content = None
json_content = json.loads(content)
request_id = json_content["buildId"]
print(request_id)

cat_links_link = f"https://alternativeto.net/_next/data/{request_id}/browse/all.json"

app_list_url = "https://alternativeto.net/_next/data/AYOFDKXQed5cMq4Zec9cA/category/ai-tools/all.json?p=1"

app_url = "https://alternativeto.net/_next/data/AYOFDKXQed5cMq4Zec9cA/software/stable-diffusion-web-ui/about.json?urlName=stable-diffusion-web-ui"

page_num = 2

curr_proxy = 0

driver = webdriver.Chrome(options=options)
driver.get(cat_links_link)

json_data = driver.find_element(By.CSS_SELECTOR, "pre").get_attribute("innerText")
driver.close()

json_data = json.loads(json_data)

all_apps_links = []

count = 0

for data_node in json_data["pageProps"]["allCategories"]["items"]:
    count += 1
    if curr_proxy == len(PROXY_LIST):
        curr_proxy = 0
    webdriver.DesiredCapabilities.CHROME["proxy"] = {
        "httpProxy": PROXY_LIST[curr_proxy],
        "ftpProxy": PROXY_LIST[curr_proxy],
        "sslProxy": PROXY_LIST[curr_proxy],
        "proxyType": "MANUAL",
    }
    curr_proxy += 1
    print(data_node["urlName"])
    driver = webdriver.Chrome(options=options)
    driver.get(
        f"https://alternativeto.net/_next/data/{request_id}/category/{data_node['urlName']}.json"
    )
    json_data = driver.find_element(By.CSS_SELECTOR, "pre").get_attribute("innerText")
    # with open("test.json", "w") as f:
    #     f.write(json_data)
    input_string = json_data

    # Find the index of the substring '2:[[' and then add the length of '2:[[' to get the start point
    start_index = input_string.find("2:[[") + len("2:[[")

    # If '2:[[' is found, slice from the start index to the end of the string
    if (
        start_index > len("2:[[") - 1
    ):  # Adjust by -1 because len('2:[[') includes the starting position
        extracted_content = input_string[start_index:]
    else:
        extracted_content = ""  # If '2:[[' is not found, return an empty string

    full_cont = f"[[{extracted_content}"
    usable_json = json.loads(full_cont)

    # print(full_cont)
    # full_cont = ast.literal_eval(full_cont)
    # with open("test.json", "w") as f:
    #     f.write(
    #         json.dumps(
    data_list = usable_json[1][3]["children"][2][3]["children"][7][3]["children"][1][3][
        "children"
    ][0]
    #     )
    # )

    for data in data_list:
        # with open("test.json", "w") as f:
        #     f.write(json.dumps(data))
        cat_name = data[3]["children"][3]["children"][3]["children"][0][3]["children"][
            3
        ][3]["children"][0][3]["children"]
        link = data[3]["children"][3]["children"][3]["children"][0][3]["children"][3][
            3
        ]["children"][0][3]["href"]
        metrics_data = data[3]["children"][3]["children"][3]["children"][1][3][
            "children"
        ]
        all = {
            "cat_name": cat_name,
            "metrics_data": metrics_data,
            "link": link,
        }
        # print(f"this is it {cat_name}")
        # print("".join(str(item) for item in metrics_data))
        # print(link)
        print(all["link"])
        usable_link = all["link"].split("/")[3]
        print(f"this is usable link {usable_link}")
        driver = webdriver.Chrome(options=options)
        driver.get(
            f"https://alternativeto.net/_next/data/{request_id}/category/{data_node['urlName']}/{usable_link}.json"
        )
        try:
            json_data_0 = driver.find_element(By.CSS_SELECTOR, "pre").get_attribute(
                "innerText"
            )
        except:
            continue
        driver.close()
        json_data_0 = json.loads(json_data_0)
        name = json_data_0["pageProps"]["meta"]["h1Title"]
        description = json_data_0["pageProps"]["meta"]["htmlMetaDesc"]
        if "All apps in the " in description:
            description = f"{name} is a subcategory of the {data_node['name']} category"
        total_apps = json_data_0["pageProps"]["pagingMeta"]["totalCount"]
        category_url = f"https://alternativeto.net{all['link']}"
        total_reviews = all["metrics_data"][-4]
        SCRAPING_DATE = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        full_data = {
            "category_name": name,
            "category_description": description,
            "total_apps_in_category": total_apps,
            "total_reviews": total_reviews,
            "category_url": category_url,
            "scraped_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        print(full_data)
        with open("alttocategoriesdata.json", "a") as f:
            f.write(json.dumps(full_data) + "\n")


with psycopg2.connect(
    database="market_data",
    user="elorm",
    password="elorm",
    host="localhost",
    port="5432",
) as conn:
    with conn.cursor() as cursor:
        with open("alttocategoriesdata.json", "r") as f:
            for line in f:
                data = json.loads(line)
                cursor.execute(
                    """insert into alternativeto_categories (name, description, total_apps, total_reviews, url, scraped_time) values
                                    (%s, %s, %s, %s, %s, %s)""",
                    (
                        data["category_name"],
                        data["category_description"],
                        data["total_apps_in_category"],
                        data["total_reviews"],
                        data["category_url"],
                        data["scraped_time"],
                    ),
                )
        # Commit the insert
        conn.commit()

print("data inserted into database")

os.remove("alttocategoriesdata.json")

print("file removed")

driver.quit()
