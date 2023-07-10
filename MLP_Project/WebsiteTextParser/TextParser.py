# beauty_soup.py

from bs4 import BeautifulSoup
from urllib.request import urlopen

def parser(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup