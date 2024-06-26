import logging
import os
import feedsearch
from config import Config

feedSearch_logger = logging.getLogger(__name__) 

def fetch_rss_link(links) -> None:
    """Locate the RSS or ATOM feed based on base url"""
    urls: list[str] = []
    for link in links:
        feed: str = feedsearch.search(link)   
        urls.append(feed)
        
    feedSearch_logger.info(f"Found {urls}")

def main():
    dir_name: str = os.path.dirname(p=__file__)
    config_file = os.path.join(dir_name, "config.toml")
    config = Config(config_file)
    links: any = config['bot']['urls']['websites']
    fetch_rss_link(links)

if __name__=="__main__":
    main()