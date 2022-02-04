import requests
from time import strftime
from bs4 import BeautifulSoup
import pandas as pd
import os

'''
Encapsulate your work in a function named get_blog_articles that will return a list of dictionaries,
 with each dictionary representing one article. The shape of each dictionary should look like this:

{
    'title': 'the title of the article',
    'content': 'the full text content of the article'
}

'''

def get_front_page_articles():
    # Set link and use soup to help dive into the code
    headers = {"User-Agent" : "Codeup Blogs"}
    response = requests.get("https://codeup.com/blog/", headers = headers)

    soup = BeautifulSoup(response.text)

    links = [link.attrs["href"] for link in soup.select(".more-link")]

    return links


def parse_blogs(url):
    #Given a blog url, extract info and return as a dictonary
    response = requests.get(url, headers = {"User-Agent": "Codeup Blog"})
    soup = BeautifulSoup(response.text)
    return {
        "title": soup.select_one(".entry-title").text,
        "published": soup.select_one(".published").text,
        "content": soup.select_one(".entry-content").text.strip()
    }

def get_blog_articles():
    # Return a datafram where each row is a blog post from codeup
    links = get_front_page_articles()
    df = pd.DataFrame([parse_blogs(link) for link in links])

    return df


# This is for inshorts news articles!
#--------------------------------------------------

def parse_news_card(card):
    # returns infor abouts a specific news card
    card_title = card.select_one('.news-card-title')

    output = {}
    output['title'] = card.find('span', itemprop = 'headline').text
    output['author'] = card.find('span', class_ = 'author').text
    output['content'] = card.find('div', itemprop = 'articleBody').text
    output['date'] = card.find('span', clas = 'date').text
    return output


def parse_inshort_page(url):
    # given a url, returna  dataframe

    category = url.split('/')[-1]
    response = requests.get(url, headers = {'user-agent' : 'codeup inshorts'})
    soup = BeautifulSoup(response.text)
    cards = soup.select('.news-card')
    df = pd.DataFrame([parse_news_card(card) for card in cards])
    df['category'] = category
    return df

def get_inshorts_articles():
    # return dataframe of the news articles in inshorts for business/ sports/ technology/ and entertainment sections
    url = 'https://inshorts.com/en/read/'
    categories = ['business', 'sports', 'technology', 'entertainment']
    df = pd.DataFrame()
    for cat in categories:
        df = pd.concat([df, pd.DataFrame(parse_inshort_page(url + cat))])
    
    df = df.reset_index(drop = True)
    return df

def save_as_json():
    today = strftime('%Y-%m-%d')
    return get_inshorts_articles().to_json(f'inshorts-{today}.json')