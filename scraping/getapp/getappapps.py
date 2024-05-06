import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
import datetime
import json
import random
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

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

proxiesf = {
    "http": random.choice(PROXY_LIST),
    "https": random.choice(PROXY_LIST),
}


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

webdriver.DesiredCapabilities.CHROME["proxy"] = {
    "httpProxy": random.choice(PROXY_LIST),
    "ftpProxy": random.choice(PROXY_LIST),
    "sslProxy": random.choice(PROXY_LIST),
    "proxyType": "MANUAL",
}

SCRAPING_DATE = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

driver = webdriver.Chrome(options=options)

url = "https://www.getapp.com/browse/"

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

all_cat = []

for category in json_content["props"]["pageProps"]["appData"]["categories"]:
    category_url = category["cta_urls"]["detail"]
    all_cat.append(category_url)

print("ALL CATEGORIES: ", len(all_cat))

page_num = 2

# test_url = f"https://www.getapp.com/_next/data/{request_id}/serp.json?header={category.split("/")[1]}&categorySlug={category.split("/")[2]}&pagination={page_num}"


def process_category(category, options):
    cat1 = category.split("/")[1]
    cat2 = category.split("/")[2]
    driver = webdriver.Chrome(options=options)
    furl = f"https://www.getapp.com/{cat1}/{cat2}/"
    print("START URL FOR THIS CATEGORY: ", furl)
    driver.get(furl)

    page_content = driver.page_source
    soup = BeautifulSoup(page_content, "html.parser")
    script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
    content = script_tag.string.strip() if script_tag else None

    try:
        json_content = json.loads(content)
    except:
        return

    try:
        test_name = json_content["props"]["pageProps"]["serpData"]["listings"][0][
            "name"
        ]
    except:
        return

    for app in json_content["props"]["pageProps"]["serpData"]["listings"]:
        name = app["name"]
        description = app["description"]
        average_ratings = app["rating_avg"]
        reviews = app["num_reviews"]
        category = f"{cat1} - {cat2}"
        domain = f'https://www.getapp.com{app["cta_urls"]["cta"]}'
        app_url = f'https://www.getapp.com{app["cta_urls"]["detail"]}'
        if domain == app_url:
            domain = "N/A"
        scraped_time = SCRAPING_DATE

        full_data = {
            "name": name,
            "description": description,
            "average_ratings": average_ratings,
            "reviews": reviews,
            "category": category,
            "domain": domain,
            "app_url": app_url,
            "scraped_time": scraped_time,
        }
        print(full_data)
        with open("getappappstest.json", "a") as f:
            f.write(json.dumps(full_data) + "\n")
        print("done writing")

    page_num = 2
    while True:
        try:
            furl = f"https://www.getapp.com/{cat1}/{cat2}/page-{page_num}/"
            print("START URL FOR THIS CATEGORY: ", furl)
            driver = webdriver.Chrome(options=options)
            driver.get(furl)

            page_content = driver.page_source
            soup = BeautifulSoup(page_content, "html.parser")
            script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
            content = script_tag.string.strip() if script_tag else None

            try:
                json_content = json.loads(content)
            except:
                break

            for app in json_content["props"]["pageProps"]["serpData"]["listings"]:
                name = app["name"]
                description = app["description"]
                average_ratings = app["rating_avg"]
                reviews = app["num_reviews"]
                category = f"{cat1} - {cat2}"
                domain = f'https://www.getapp.com{app["cta_urls"]["cta"]}'
                app_url = f'https://www.getapp.com{app["cta_urls"]["detail"]}'
                if domain == app_url:
                    domain = "N/A"
                scraped_time = SCRAPING_DATE

                full_data = {
                    "name": name,
                    "description": description,
                    "average_ratings": average_ratings,
                    "reviews": reviews,
                    "category": category,
                    "domain": domain,
                    "app_url": app_url,
                    "scraped_time": scraped_time,
                }
                print(full_data)
                with open("getappappstest.json", "a") as f:
                    f.write(json.dumps(full_data) + "\n")
            page_num += 1
        except Exception as e:
            page_num = 2
            print(e)
            break


with ThreadPoolExecutor(max_workers=15) as executor:
    executor.map(lambda category: process_category(category, options), all_cat)

# for category in all_cat:
#     cat1 = category.split("/")[1]
#     cat2 = category.split("/")[2]
#     driver = webdriver.Chrome(options=options)
#     # furl = f"https://www.getapp.com/_next/data/{request_id}/serp.json?header={category.split('/')[1]}&categorySlug={category.split('/')[2]}"
#     furl = f"https://www.getapp.com/{cat1}/{cat2}/"
#     print("START URL FOR THIS CATEGORY: ", furl)
#     driver.get(furl)

#     page_content = driver.page_source

#     soup = BeautifulSoup(page_content, "html.parser")

#     script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
#     if script_tag:
#         content = script_tag.string.strip()
#     else:
#         content = None
#     try:
#         json_content = json.loads(content)
#     except:
#         break

#     # if not json_content["props"]["pageProps"]["serpData"]["listings"]:
#     #     break
#     try:
#         test_name = json_content["props"]["pageProps"]["serpData"]["listings"][0][
#             "name"
#         ]
#     except:
#         break

#     for app in json_content["props"]["pageProps"]["serpData"]["listings"]:
#         name = app["name"]
#         description = app["description"]
#         average_ratings = app["rating_avg"]
#         reviews = app["num_reviews"]
#         category = f"{cat1} - {cat2}"
#         domain = f'https://www.getapp.com{app["cta_urls"]["cta"]}'
#         app_url = f'https://www.getapp.com{app["cta_urls"]["detail"]}'
#         if domain == app_url:
#             domain = "N/A"
#         scraped_time = SCRAPING_DATE

#         full_data = {
#             "name": name,
#             "description": description,
#             "average_ratings": average_ratings,
#             "reviews": reviews,
#             "category": category,
#             "domain": domain,
#             "app_url": app_url,
#             "scraped_time": scraped_time,
#         }
#         print(full_data)
#         with open("getappappstest.json", "a") as f:
#             f.write(json.dumps(full_data) + "\n")
#         print("done writing")
#     while True:
#         print("entered while loop")
#         try:
#             furl = f"https://www.getapp.com/{cat1}/{cat2}/page-{page_num}/"
#             print("START URL FOR THIS CATEGORY: ", furl)
#             driver = webdriver.Chrome(options=options)
#             driver.get(furl)

#             page_content = driver.page_source

#             soup = BeautifulSoup(page_content, "html.parser")

#             script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
#             if script_tag:
#                 content = script_tag.string.strip()
#             else:
#                 content = None
#             # reqUrl = "https://www.getapp.com/_next/data/srqSurnxMKHkpO6PFHSR9h0dFZg/serp.json?header=all&categorySlug=vaccine-management-software&pagination=2"
#             # reqUrl = f"https://www.getapp.com/_next/data/{request_id}/serp.json?header={cat1}&categorySlug={cat2}&pagination={page_num}"
#             # print("THIS IS THE NEXT JSON URL: ", reqUrl)
#             # headersList = {
#             #     "'accept'": "'*/*',",
#             #     "'accept-language'": "'en-US,en;q=0.8',",
#             #     "'cookie'": "'v_exp_serp-ugc-experiment=0; gauid=ZHMVgmX52a6+CQAJNHxEAg==; v_exp_serp-ugc-v-2-experiment=0; ld_context_uuid=cb474c53-8e71-49dd-9853-bb05e8acb265; v_exp_listing-detail-exit-intent=1; compareBasket=%5B%5D; v_exp_listing-detail-exit-intent-v-2=1; most_visited_apps_for_serp_570_1=c7f00a1b-c5c0-4be8-8c9b-a6d200b37696&e3d6d43b-3d5e-4498-9672-a6d200b2bfa3&dd850fc3-3264-45b5-bd6e-a6d200b7915e; most_visited_apps_for_serp_570_2=16519578-e04c-472a-92fc-a76a00349b71&953d0def-d4c2-4ecc-aa69-a6d200b7c72b&3c11cdb2-2af9-4893-9f1a-a6d200b6e7b3; most_visited_apps_for_serp_1483_2=; getapp.session=64029c62fd6738d6ec7d192d86fa8808; __cf_bm=TX6Bf2UADQ_G0a4ceidq1Bt8GLfN.meuFMY9nY7vxY0-1714821926-1.0.1.1-p36aZoteSyoGTZt8kEZQpjN45ZZgghFdNmzucSs3PYWuRaml2oC8DO1DiCn6c8JCpahYk.1HvzgRdXy_N3UQqA; cf_clearance=smzUkBZiZgkiCez8Sq9sMMaJTjR8TEas9oEH03R7w80-1714821930-1.0.1.1-JDtqfF4n8mZSpvMr3Yavbcu_gmFH0NXl_hkxvxjzZA7jxiRBW1LuhTZ4l90YkwLzS_6RPbKSWWaHZoHx_jY_YA; most_visited_apps_for_serp_3759_1=; _dd_s=rum=0&expire=1714822981910&logs=1&id=c67f5c44-65ca-4bb1-a211-41a0a6c54b13&created=1714815469800',",
#             #     "'priority'": "'u=1, i',",
#             #     "'referer'": "'https://www.getapp.com/all-software/vaccine-management-software/',",
#             #     "'sec-ch-ua-mobile'": "'?0',",
#             #     "'sec-fetch-dest'": "'empty',",
#             #     "'sec-fetch-mode'": "'cors',",
#             #     "'sec-fetch-site'": "'same-origin',",
#             #     "'sec-gpc'": "'1',",
#             #     "'user-agent'": "'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',",
#             #     "'x-nextjs-data'": "'1',",
#             # }
#             # cookies = {
#             #     "v_exp_serp-ugc-experiment": "0",
#             #     "gauid": "ZHMVgmX52a6+CQAJNHxEAg==",
#             #     "v_exp_serp-ugc-v-2-experiment": "0",
#             #     "ld_context_uuid": "cb474c53-8e71-49dd-9853-bb05e8acb265",
#             #     "v_exp_listing-detail-exit-intent": "1",
#             #     "compareBasket": "%5B%5D",
#             #     "v_exp_listing-detail-exit-intent-v-2": "1",
#             #     "most_visited_apps_for_serp_570_1": "c7f00a1b-c5c0-4be8-8c9b-a6d200b37696&e3d6d43b-3d5e-4498-9672-a6d200b2bfa3&dd850fc3-3264-45b5-bd6e-a6d200b7915e",
#             #     "most_visited_apps_for_serp_570_2": "16519578-e04c-472a-92fc-a76a00349b71&953d0def-d4c2-4ecc-aa69-a6d200b7c72b&3c11cdb2-2af9-4893-9f1a-a6d200b6e7b3",
#             #     "most_visited_apps_for_serp_1483_2": "",
#             #     "getapp.session": "64029c62fd6738d6ec7d192d86fa8808",
#             #     "cf_clearance": "smzUkBZiZgkiCez8Sq9sMMaJTjR8TEas9oEH03R7w80-1714821930-1.0.1.1-JDtqfF4n8mZSpvMr3Yavbcu_gmFH0NXl_hkxvxjzZA7jxiRBW1LuhTZ4l90YkwLzS_6RPbKSWWaHZoHx_jY_YA",
#             #     "most_visited_apps_for_serp_3759_1": "",
#             #     "__cf_bm": "q3qGfZQeRJ2GPQClDjRumnpRITR9Zej9jmx.0S5vhu0-1714823771-1.0.1.1-hRyykkRH7PzCCQdFBlxMLwvSXlMvckfPD4BoGC9NOm4_45MtzmPxcagcP3GVxtN5Z.Z4Vb_AAZOlTJYNRHJhjQ",
#             #     "most_visited_apps_for_serp_332_1": "c7f00a1b-c5c0-4be8-8c9b-a6d200b37696&e3d6d43b-3d5e-4498-9672-a6d200b2bfa3&dd850fc3-3264-45b5-bd6e-a6d200b7915e",
#             #     "_dd_s": "rum=0&expire=1714824717056&logs=1&id=4e93886a-af56-459a-a2f4-a5a7ccb3c86b&created=1714823800537",
#             # }

#             # payload = ""

#             # response = requests.get(
#             #     reqUrl,
#             #     data=payload,
#             #     headers=headersList,
#             #     proxies=proxiesf,
#             #     cookies=cookies,
#             # )
#             # print("request made")

#             # print("RESPONSE: ", response)

#             # print(response.text)
#             try:
#                 json_content = json.loads(content)
#             except:
#                 break
#             print("JSON CONTENT: ", json_content)

#             # if not json_content["props"]["pageProps"]["serpData"]["listings"]:
#             #     break
#             try:
#                 test_name = json_content["props"]["pageProps"]["serpData"]["listings"][
#                     0
#                 ]["name"]
#             except:
#                 break

#             for app in json_content["props"]["pageProps"]["serpData"]["listings"]:
#                 name = app["name"]
#                 description = app["description"]
#                 average_ratings = app["rating_avg"]
#                 reviews = app["num_reviews"]
#                 # category = app["cta_urls"]["detail"].split("/")[3]
#                 category = f"{cat1} - {cat2}"
#                 domain = f'https://www.getapp.com{app["cta_urls"]["cta"]}'
#                 app_url = f'https://www.getapp.com{app["cta_urls"]["detail"]}'
#                 if domain == app_url:
#                     domain = "N/A"
#                 scraped_time = SCRAPING_DATE

#                 full_data = {
#                     "name": name,
#                     "description": description,
#                     "average_ratings": average_ratings,
#                     "reviews": reviews,
#                     "category": category,
#                     "domain": domain,
#                     "app_url": app_url,
#                     "scraped_time": scraped_time,
#                 }
#                 print(full_data)
#                 with open("getappappstest.json", "a") as f:
#                     f.write(json.dumps(full_data) + "\n")
#             # # url = f"https://www.getapp.com{category}page-{page_num}/"
#             # url = f"https://www.getapp.com/_next/data/{request_id}/serp.json?header={cat1}&categorySlug={cat2}&pagination={page_num}"

#             # print("THIS IS THE NEXT JSON URL: ", url)
#             # driver = webdriver.Chrome(options=options)

#             # driver.get(url)

#             # page_content = driver.page_source

#             # soup = BeautifulSoup(page_content, "html.parser")

#             # script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
#             # if script_tag:
#             #     content = script_tag.string.strip()
#             # else:
#             #     content = None
#             # try:
#             #     json_content = json.loads(content)
#             # except:
#             #     break

#             # # if not json_content["props"]["pageProps"]["serpData"]["listings"]:
#             # #     break
#             # try:
#             #     test_name = json_content["props"]["pageProps"]["serpData"]["listings"][
#             #         0
#             #     ]["name"]
#             # except:
#             #     break

#             # for app in json_content["props"]["pageProps"]["serpData"]["listings"]:
#             #     name = app["name"]
#             #     description = app["description"]
#             #     average_ratings = app["rating_avg"]
#             #     reviews = app["num_reviews"]
#             #     category = app["cta_urls"]["detail"].split("/")[1]
#             #     domain = f'https://www.getapp.com{app["cta_urls"]["cta"]}'
#             #     app_url = f'https://www.getapp.com{app["cta_urls"]["detail"]}'
#             #     if domain == app_url:
#             #         domain = "N/A"
#             #     scraped_time = SCRAPING_DATE

#             #     full_data = {
#             #         "name": name,
#             #         "description": description,
#             #         "average_ratings": average_ratings,
#             #         "reviews": reviews,
#             #         "category": category,
#             #         "domain": domain,
#             #         "app_url": app_url,
#             #         "scraped_time": scraped_time,
#             #     }
#             #     print(full_data)
#             #     with open("getappapps.json", "a") as f:
#             #         f.write(json.dumps(full_data) + "\n")

#             page_num += 1

#             # driver.close()

#         except Exception as e:
#             page_num = 2
#             print(e)
#             break
#     page_num = 2
