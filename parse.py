from datetime import datetime
import logging
import feedparser

parser_logger = logging.getLogger(__name__) 

def fetch_rss_data(urls):
    """Collect recent articles found on RSS or ATOM link"""
    # Get current year and current month
    current_year = datetime.now().year
    current_month = datetime.now().month

    # parse
    for url in urls:
        feed = feedparser.parse(url)
        if len (feed) > 0:
            parser_logger.info(f"RSS {url} parsed")
            try:
                for entry in feed.entries:
                    date = entry.published_parsed
                    if date.tm_year == current_year and date.tm_mon == current_month:
                        print("Entry Title:", entry.title)
                        print("Entry Author:", entry.author)
                        print("Entry Link:", entry.link)
                        print("Entry Published Date:", entry.published)
                        print("Entry Summary:", entry.summary)
                        print("\n")
                        parser_logger.info(f"Article contents extracted. title:{entry.title} published date {entry.publshed}")
            except: AttributeError
            parser_logger.exception(f"Nothing found at {url}")
def main():
    url = "https://www.theverge.com/rss/index.xml"
    fetch_rss_data(url)


if __name__ == "__main__":
    main()

