import requests
from bs4 import BeautifulSoup

WOWHEAD_URL = 'https://www.wowhead.com/wow/retail'
last_parsed_news = []

def get_latest_news(count=3):
    response = requests.get(WOWHEAD_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    news_cards = soup.find_all('div', class_='news-list-card')[3:3+count]
    news_list = []
    
    for card in news_cards:
        link = "https://www.wowhead.com" + card.find('a')['href']
        title = card.find('h3').text.strip()
        description = card.find('div', class_='news-list-card-content-body').text.strip()
        author = card.find('div', class_='news-list-card-content-footer').text.strip()
        news_list.append({
            'link': link,
            'title': title,
            'description': description,
            'author': author
        })

    return news_list

def check_for_new_news():
    global last_parsed_news
    new_news = get_latest_news(1)
    
    if new_news:
        new_news = new_news[0]
        if new_news not in last_parsed_news:
            last_parsed_news.append(new_news)
            if len(last_parsed_news) > 5: 
                last_parsed_news.pop(0)
            return new_news
    return None
