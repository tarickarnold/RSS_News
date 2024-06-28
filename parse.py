from datetime import datetime
import logging
import feedparser

parser_logger = logging.getLogger(__name__) 

def fetch_rss_data(url):
    """Collect recent articles found on RSS or ATOM link"""
    # Get current year and current month
    current_year = datetime.now().year
    current_month = datetime.now().month

    # parse
    feed = feedparser.parse(url)
    parser_logger.info("RSS parsed")
    for entry in feed.entries:
        date = entry.published_parsed
        if date.tm_year == current_year and date.tm_mon == current_month:
            parser_logger.info("Articles sorted by month and year")
            print("Entry Title:", entry.title)
            print("Entry Author:", entry.author)
            print("Entry Link:", entry.link)
            print("Entry Published Date:", entry.published)
            print("Entry Summary:", entry.summary)
            print("\n")
            # parser_logger.info(f"Article contents extracted. title:{entry.title},
            # author:{entry.author}, link:{entry.link}, published_date:{entry.published}")                                )

def main():
    url = "https://www.theverge.com/rss/index.xml"
    fetch_rss_data(url)


if __name__ == "__main__":
    main()

