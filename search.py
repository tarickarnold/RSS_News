import logging
import os
from bs4 import BeautifulSoup
import requests
from config import Config

search_logger = logging.getLogger(__name__) 

def fetch_rss_links(links)-> list:
    urls: list = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    for link in links:
        response = requests.get(url= link, headers= headers).text
        html = BeautifulSoup(response, 'lxml')
        feed_urls = html.find_all("link", rel="alternate", 
        type = ["application/atom+xml", "application/rss+xml", "application/rss.xml"])
        
        try:
            for f in feed_urls:
                if "rss" or "xml" or "feed" in f:
                    href = f.get("href", None)
                    if "https://" not in href:
                        full_url = link+href
                        urls.append(full_url)
                        search_logger.info(f"Link combined link and href: {full_url}")
                    else:
                        urls.append(href)
                        search_logger.info(f"Found url: {href}")
        except AttributeError as e:
            search_logger.exception(f"{e}")

    return urls

#TODO Add function to clean up list of functional urls

def main():
    dir_name: str = os.path.dirname(p=__file__)
    config_file = os.path.join(dir_name, "config.toml")
    config = Config(config_file)
    links: any = config['bot']['urls']['websites']
    fetch_rss_links(links=links)

if __name__=="__main__":
    main()