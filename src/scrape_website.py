import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_wine_page_links(page_number):
    # use get a set of links for each bottle of wine
    url_path = "https://www.argonautliquor.com/search/sort/rating%20desc/categories/Wine/sort/rating%20desc/page/"
    full_url = url_path + str(page_number)
    page = requests.get(full_url)
    soup = BeautifulSoup(page.text)

    # gather website links
    links = []
    wine_page = soup.find_all("div", {"class": "col", "role": "link"})
    for tag in wine_page:
        links.append(tag["data-href"])

    return links


if __name__ == "__main__":
    all_links = []
    i = 1
    while i < 5:
        all_links.append(get_wine_page_links(i))
        i += 1
