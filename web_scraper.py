import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_same_domain(base_url, link):
    return urlparse(base_url).netloc == urlparse(link).netloc

def scrape_page(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return None, []
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup(["script", "style"]):
            tag.decompose()

        text = soup.get_text(separator=' ')
        text = ' '.join(text.split())

        links = set()
        for a_tag in soup.find_all('a', href=True):
            full_link = urljoin(url, a_tag['href'])
            if is_same_domain(url, full_link):
                links.add(full_link)

        return text, links
    except Exception as e:
        print(f"[Error] {url} — {e}")
        return None, []

def crawl_website(start_url, max_pages=10):
    visited = set()
    to_visit = [start_url]
    all_content = ""

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue

        print(f"Scraping: {url}")
        text, links = scrape_page(url)
        if text:
            all_content += text + "\n\n"
        visited.add(url)
        to_visit.extend(links - visited)

    return all_content