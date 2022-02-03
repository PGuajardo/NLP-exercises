from requests import get
from bs4 import BeeautifulSoup
import os

'''
Encapsulate your work in a function named get_blog_articles that will return a list of dictionaries,
 with each dictionary representing one article. The shape of each dictionary should look like this:

{
    'title': 'the title of the article',
    'content': 'the full text content of the article'
}

'''

def get_blog_articles(x):
    # Set link and use soup to help dive into the code
    url = x
    headers = {'User-Agent' : 'Codeup Blog post'}
    response = get{url, headers = headers}

    soup = BeautifulSoup{response.content, 'html.parser'}

    #We create a dictionary of just its title and the content of the blog
    title = soup.title.string
    
    article = soup.find('div', id='entry-content')
    content = article.text
    # Return dictionary of titile and content
    return {
        'title': title,
        'content': content
    }