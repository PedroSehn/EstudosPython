import requests
from parsel import Selector
from datetime import datetime
import re

def get_items(url):
    resp = requests.get(url,
                        headers={"user-agent": "Fake user-agent"},
                        timeout=3)
    return resp.text


def scrape_updates(html_content):
    selector = Selector(text=html_content)
    articles = selector.css('article').getall()
    links = []
    for index, article in articles:
        links.append(selector.xpath(
            f'//*[@id="main"]/div/div/div/article[{index}]/div/div[2]/header/h2/a'))
    return links


def scrape_news(html_content):
    info_dict = {}
    selector = Selector(text=html_content)
    info_dict['url'] = selector.css(
        "head > link[rel='canonical']::attr(href)").get()
    info_dict['title'] = selector.css(".entry-title::text").get().strip()
    info_dict['timestamp'] = selector.css('.meta-date::text').get()
    info_dict['writer'] = selector.css("span[class='author'] > a::text").get()
    tempo_leitura = selector.css("li[class='meta-reading-time']::text").get()
    info_dict['reading_time'] = int(re.findall(r'\d+', f"{tempo_leitura}")[0])
    sumary = selector.css(".entry-content > p:nth-of-type(1) *::text ").getall()
    info_dict['summary'] = ''.join(sumary).strip()
    info_dict['category'] = selector.css(".category-style .label::text").get()
    return info_dict


def date_test(date):
    data_formed_date = datetime.strptime(date, "%Y-%m-%d")
    return data_formed_date.strftime('%d/%m/%Y')


print(date_test('2000-03-01'))