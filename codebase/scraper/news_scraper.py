import requests
from bs4 import BeautifulSoup
from GoogleNews import GoogleNews

from codebase.models.source import Source


def get_links(search_term, time_period = '1d'):
    googlenews = GoogleNews(period=time_period)
    googlenews.search(search_term)
    results = googlenews.results()
    links = [result['link'] for result in results]
    return links

def clean_link(link):
    return link.split('&')[0]

def get_text_from(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    source_text = ''.join([str(s) for s in soup.find_all(string=True) if s.parent.name not in ['style', 'script']])
    return source_text

def clean_text(html_text):
    cleaned_html_text = html_text.strip().replace('\n', ' ').replace('\r', '')
    return cleaned_html_text[:10_000]
    
def build_sources_from(question, n_sources = 3):
    links = get_links(question)
    sources = []
    for link in links[:n_sources]:
        cleaned_link = clean_link(link)
        text = get_text_from(cleaned_link)
        source = Source(text = text, url = cleaned_link)
        sources.append(source)
    return sources
    
    