import requests
from bs4 import BeautifulSoup
from GoogleNews import GoogleNews

from codebase.models.source import Source


def get_links(search_term, time_period = '1d'):
    pass

def clean_link(link):
    pass

def get_text_from(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    source_text = ''.join([str(s) for s in soup.find_all(string=True) if s.parent.name not in ['style', 'script']])
    return source_text

def clean_text(html_text):
    pass
    
def build_sources_from(question, n_sources = 3):
    pass
    
    