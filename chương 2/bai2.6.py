import feedparser as f
import csv

# URL của RSS feed
rss_url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

feed = f.parse(rss_url)
with open("rss_feed.xml", "w", encoding="utf-8") as xml_file:
    xml_file.write(feed.to_xml())

news_items = []
for entry in feed.entries:
    news_item = {
        "title": entry.title,
        "link": entry.link,
        "published": entry.published,
        "summary": entry.summary
    }
    news_items.append(news_item)

csv_file_path = "rss_feed.csv"
csv_fields = ["title", "link", "published", "summary"]

with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=csv_fields)
    
    csv_writer.writeheader()
    
    csv_writer.writerows(news_items)

print(f"Đã lưu thông tin tin tức vào tệp CSV: {csv_file_path}")