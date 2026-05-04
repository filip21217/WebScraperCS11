import os
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

product_code = input("Provide product code: ")
page = 1
next = True

headers ={
    "Host": "www.ceneo.pl",
    "Cookie": "__RequestVerificationToken=2zeSEbWAvn9A5jqABwRXDse96XZkYieNtXN8SK5dRMUfykatUXAP1YURiyx5CittHoRHgbKJEzTcr1FPW66q4VaOm3cvDTqEBYppbp42I_k1; __utmf=fce045a5017285d45350b8aaf2d86854_Dsgqi6QMc9CtX7buqOpcIw%3D%3D; sv3=2.0_49fc079f-47b2-11f1-913d-0126a848b088_1777896649620; userCeneo=ID=f490d972-332b-4a16-8016-ae0ab8363d05; ai_user=BhRaH|2026-05-04T12:10:49.915Z; appType=%7B%22Value%22%3A1%7D; cProdCompare_v2=; browserBlStatus=0; ga4_ga=GA1.2.49fc079f-47b2-11f1-913d-0126a848b088; _gcl_au=1.1.335257580.1777896653; consentcookie=eyJBZ3JlZUFsbCI6dHJ1ZSwiQ29uc2VudHMiOlsxLDMsNCwyXSwiVENTdHJpbmciOiJDUWpyczhBUWpyczhBR3lBQkJQTENkRXNBUF9nQUFBQUFCNVlLTHREN0Q3ZExXRmd3SHhuWUtzUU1JMWY4ZUNBWW9RQUJBYUJBU0FCU0FLUUlJUUdra0FRSkFTZ0JBQUNBQUlBS0NSQklRQU1BQUNBQ0VBQVFJQUFJUUFFQUFDUUFRZ0tBQUFFaUFBUUFBQVlBQUFpQ0lBQUFRQUlnRUlFRUJFQW1RaEFBQUlBRUZBQWpBQUVJQUFBQUFBQUFBQUFBd0FBQUFBQ0FBSUFBQUFBZ0NBQUFJQUFBQUFBQUVBQVFCZ0lFQUFBQUFFQUFBQUFBQUFBQVFBQUFCQUFBQUFJS0xnQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUJZS0FEQUFFRkZ3a0FHQUFJS0xob0FNQUFRVVhFUUFZQUFnb3VLZ0F3QUJCUmNaQUJnQUNDaTQ2QURBQUVGRnlFQUdBQUlLTGtvQU1BQVFVWEtRQVlBQWdvdVdnQXdBQkJSY0EuSUtMdEQ3RDdkTFdGZ3dIeG5ZS3NRTUkxZjhlQ0FZb1FBQkFhQkFTQUJTQUtRSUlRR2trQVFKQVNnQkFBQ0FBSUFLQ1JCSVFBTUFBQ0FDRUFBUUlBQUlRQUVBQUNRQVFnS0FBQUVpQUFRQUFBWUFBQWlDSUFBQVFBSWdFSUVFQkVBbVFoQUFBSUFFRkFBakFBRUlBQUFBQUFBQUFBQUF3QUFBQUFDQUFJQUFBQUFnQ0FBQUlBQUFBQUFBRUFBUUJnSUVBQUFBQUVBQUFBQUFBQUFBUUFBQUJBQUFBQUlBIiwiVmVyc2lvbiI6InYzIn0=; FPID=FPID2.2.Wj6cbbhtwO5PbhnhAv264zs2zKsX%2FtIJZA%2Bp0V%2Fn%2Buw%3D; FPLC=INHB7YKw9ta45ZIA2utek1MGZaN84AjEc%2FTogU7M7qTHagAhacWDbRkvBmnnHp9MXrs15hTMof%2Fu%2FFpSsmNa2UAnA72nXc1yCT8yQkpRa6vOuvY%3D; cto_bundle=MSR8xV85NDRiVENibTJVRUMxYzJ5aXByJTJCQ0pDaHdBUmpXSDBocndUeXNFaFcwS21tTFgyZHA0NnlJS2c3RW1Ubng1UGtQS3RGbkw0c1Vpbk03ckQ3dmJOVmtuayUyQkV6TU5JRUJFJTJGRmtpY1NWYWU3OHNHMmNFcEoyVXFFSUpyT2JjSzYyVg; _tt_enable_cookie=1; _ttp=01KQSECKF7RWMDZP4VFFMF51MT_.tt.1; __gads=ID=b297ae9f433fa34c:T=1777896672:RT=1777896672:S=ALNI_MYE8LKxuG7KUUYcQEqdtTbBDpOFWA; __gpi=UID=000013b42496cfbc:T=1777896672:RT=1777896672:S=ALNI_MZB4oVVnya2BjOCjWgWbvDsOKX4gg; __eoi=ID=080bb99d52f3cb9f:T=1777896672:RT=1777896672:S=AA-AfjZ5dipZ1Bj-0bfg_Sx1OkPz; _fbp=fb.1.1777896672927.960320613151659749; captcha=nUnCU6F5cnXzEASFEXTt9zsFt62AiNVEWcPxBBrK91wjenp6TQ1CFMF49ooyGuyOZmTjvzISimsmTSWz4EwlQ5yLE51CyPl%2BGhJifkphAfVzQxHQwAYVa2jD0VA%2B%2FLJTgikAokL3%2BlzjvOoZ0xfx8N5XdaIys%2B%2Fed1LneF9fRFNR3rtrk9pugogt03Ia9CRbHd5fcv9CrY8%3D; rc=igdamb4ThOT/AObseYIgrEpeFsMflKvy/mMe/slf8I+qp8ZzLphHf8JnqS0eypifulCz02+2uwmk6rO+DotsrytFha4ztfatFXyOkF429OLLQS2sjY9sN7pQs9NvtrsJpOqzvg6LbK8rRYWuM7X2rRV8jpBeNvTioWj5G4TXQ1MX32jeyfFNAQWCBL75GEwstChKPHUCrb15DmmZOaHMPA==; urdsc=1; nps3=SessionStartTime=1777896701,SurveyId=68; ai_session=BbJ/D|1777896650421|1777896702248.4; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22uIAuRfSHccW7l2KqJPfU%22%2C%22expiryDate%22%3A%222027-05-04T12%3A11%3A42.392Z%22%7D; __rtbh.aid=%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%2249fc079f-47b2-11f1-913d-0126a848b088%22%2C%22expiryDate%22%3A%222027-05-04T12%3A11%3A42.394Z%22%7D; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222027-05-04T12%3A11%3A42.395Z%22%7D; ttcsid_CNK74OBC77U1PP7E4UR0=1777896672745::5mYC_CWQreLmxAWqEXNG.1.1777896702508.1; ttcsid=1777896672745::MDjiYugSX9IL9JuL0NOy.1.1777896702509.0::1.28957.29764::0.0.0.0::0.0.0; ga4_ga_K2N2M0CBQ6=GS2.2.s1777896650$o1$g1$t1777896713$j60$l0$h804396496",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

url = f"https://www.ceneo.pl/{product_code}/opinie-{page}"

path_to_driver = "D:\\chromedriver-win64\\chromedriver.exe"
s = Service(path_to_driver)
driver = webdriver.Chrome(service=s)
driver.get(url)
driver.maximize_window()
driver.find_element(by="xpath", value="//*[@id='js_cookie-consent-general']/div/div[2]/button[1]").click()

all_opinions = []
while next:
    url = f"https://www.ceneo.pl/{product_code}/opinie-{page}"
    print(url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        page_dom = BeautifulSoup(response.text, 'html.parser')
        product_name = page_dom.select_one('h1').get_text() if page==1 else product_name
        print(product_name)
        opinions = page_dom.select("div.js_product-review:not(.user-post--highlight)")
        print(len(opinions))
        for opinion in opinions:
            single_opinion = {
                'opinion_id': opinion.get("data-entry-id"),
                'author': opinion.select_one("span.user-post__author-name").get_text().strip(),
                'recommendation': opinion.select_one('span.user-post__author-recomendation > em').get_text().strip() if opinion.select_one('span.user-post__author-recomendation > em') else None,
                'score': opinion.select_one('span.user-post__score-count').get_text().strip(),
                'content': opinion.select_one('div.user-post__text').get_text().strip(),
                'pros': [p.get_text().strip() for p in opinion.select('div.review-feature__item--positive')],
                'cons': [c.get_text().strip() for c in opinion.select('div.review-feature__item--negative')],
                'helpful': opinion.select_one('button.vote-yes > span').get_text().strip(),
                'unhelpful': opinion.select_one('button.vote-no > span').get_text().strip(),
                'publish_date': opinion.select_one('span.user-post__published > time:nth-child(1)').get('datetime').strip(),
                'purchase_date': opinion.select_one('span.user-post__published > time:nth-child(2)').get('datetime').strip() if opinion.select_one('span.user-post__published > time:nth-child(2)') else None,
            }
            all_opinions.append(single_opinion)
    next = True if page_dom.select_one('button.pagination__next') else False
    if next: 
        page += 1
        # element = driver.find_element(by=By.CLASS_NAME, value="pagination__next")
        # actions = ActionChains(driver)
        # actions.move_to_element(element).perform()
        # driver.find_element(by="xpath", value="//*[@id='reviews']/div/div[7]/button[3]").click()

if not os.path.exists("./opinions"):
    os.mkdir("./opinions")
with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)