import os
import json
import requests
from bs4 import BeautifulSoup

product_code = input("Provide product code: ")
page = 1
next = True

headers ={
    "Host": "www.ceneo.pl",
    "Cookie": "sv3=1.0_566eaee8-3cbb-11f1-b935-43a602f95b54; urdsc=1; userCeneo=ID=cf7af9ed-4a9d-4284-882d-dce9c9224437; __RequestVerificationToken=iTg2nnkVRrx9s5-P8aGFvi5S25fWcXdd7Svw79cp9zocktJ0Mio8W01x-7M1Ubk0535dulesNwGBXB57ofD08mIEDr-zkHJimuRT85pvxbM1; ai_user=Pu8Vy|2026-04-20T13:17:53.488Z; appType=%7B%22Value%22%3A1%7D; __utmf=3ca382d9f4bd083487b56039a7276dfe_Dsgqi6QMc9CtX7buqOpcIw%3D%3D; ai_session=uqvzP|1776691074417.8|1776691074417.8; cProdCompare_v2=; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222027-04-20T13%3A17%3A54.738Z%22%7D; __rtbh.aid=%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%22566eaee8-3cbb-11f1-b935-43a602f95b54%22%2C%22expiryDate%22%3A%222027-04-20T13%3A17%3A54.739Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22wgAe8fP6evkZ56SRTr5A%22%2C%22expiryDate%22%3A%222027-04-20T13%3A17%3A54.740Z%22%7D; browserBlStatus=0; ga4_ga=GA1.2.566eaee8-3cbb-11f1-b935-43a602f95b54; _gcl_au=1.1.1085943964.1776691078; consentcookie=eyJBZ3JlZUFsbCI6dHJ1ZSwiQ29uc2VudHMiOlsxLDMsNCwyXSwiVENTdHJpbmciOiJDUWk5ajBBUWk5ajBBR3lBQkJQTENiRXNBUF9nQUFBQUFCNVlJekpEN0JiRkxVRkF3RmhqWUtzUU1JRVRVTUNBQW9RQUFBYUJBQ0FCUUFLUUlBUUNra0FRQkFTZ0JBQUNBQUFBSUNSQklRQU1BQUFBQ0VBQVFBQUFJQUFFQUFDUUFRQUlBQUFBZ0FBUUFBQVlBQUFpQUlBQUFBQUlnQUlBRUFBQW1RaEFBQUlBRUVBQWhBQUVJQUFBQUFBQUFBQUFBZ0FBQUFBQ0FBSUFBQUFBQUNBQUFJQUFBQUFBQUFBQUFCQkdZQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFCWUtBREFBRUVaZ2tBR0FBSUl6Qm9BTUFBUVJtRVFBWUFBZ2pNS2dBd0FCQkdZWkFCZ0FDQ013NkFEQUFFRVppRUFHQUFJSXpFb0FNQUFRUm1LUUFZQUFnak1XZ0F3QUJCR1kuSUl6SkQ3QmJGTFVGQXdGaGpZS3NRTUlFVFVNQ0FBb1FBQUFhQkFDQUJRQUtRSUFRQ2trQVFCQVNnQkFBQ0FBQUFJQ1JCSVFBTUFBQUFDRUFBUUFBQUlBQUVBQUNRQVFBSUFBQUFnQUFRQUFBWUFBQWlBSUFBQUFBSWdBSUFFQUFBbVFoQUFBSUFFRUFBaEFBRUlBQUFBQUFBQUFBQUFnQUFBQUFDQUFJQUFBQUFBQ0FBQUlBQUFBQUFBQUFBQUJBIiwiVmVyc2lvbiI6InYzIn0=; FPID=FPID2.2.fiY7p9tKJFVjeP3cNvi5vjoHxiSG77DqwPwdbeICwPc%3D; ga4_ga_K2N2M0CBQ6=GS2.2.s1776691074$o1$g0$t1776691077$j60$l0$h1559572346; FPLC=fJ4SLDcUWDpzn%2F6ETuF4f04vpM2rm5ONjrcK1JeCGOGGqen9%2FTn%2FIkYGwc1gSRKYfNwdUuJBSuP%2BERjUaWICdxc5QKms6CPvYmPq4aGOKHkx6rU%3D",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
}

all_opinions = []
while next:
    url = f"https://www.ceneo.pl/{product_code}/opinie-{page}"
    print(url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        page_dom = BeautifulSoup(response.text, 'html.parser')
        product_name = page_dom.select_one('h1').get_text() if page == 1 else product_name
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
    if next: page += 1

if not os.path.exists("./opinions"):
    os.mkdir("./opinions")
with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)