import requests
from bs4 import BeautifulSoup
import re


def get_billboard_top_100(date:str) -> tuple[list, list]:
    """
    Scrapes the top 100 billboard tracks and their respective artists for a given year

    :param date: date to scrape
    :type date: str
    :return: tracks and their respective artists
    :rtype: tuple[list, list]
    """
    
    url = "https://www.billboard.com/charts/hot-100/{DATE}"

    # get html data and create soup
    response = requests.get(url=url.replace("{DATE}", date))
    soup = BeautifulSoup(response.text, 'html.parser')

    # find titles of songs
    title_elements = soup.select("li ul li h3")
    titles = [title.getText().strip() for title in title_elements]

    # find artists of songs
    pattern = re.compile(r'\bc-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only\b')
    artist_elements = soup.find_all(name="span", class_=pattern)
    artists = [artist.getText().strip() for artist in artist_elements]

    return titles, artists

