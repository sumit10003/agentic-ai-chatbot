from web_scraper import crawl_website

website_url = "https://skyberaerospace.com/"
content = crawl_website(website_url, max_pages=10)
print(content[:2000])  # Show a preview
