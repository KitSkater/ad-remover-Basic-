from bs4 import BeautifulSoup
import requests

def remove_ads(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Common ad-related patterns
    ad_selectors = [
        '[id*="ad"]',
        '[class*="ad"]',
        '[id*="sponsor"]',
        '[class*="sponsor"]'
    ]

    for selector in ad_selectors:
        for ad in soup.select(selector):
            ad.decompose()

    return str(soup)

def main():
    url = input("Enter a URL: ")
    response = requests.get(url)

    if response.status_code == 200:
        clean_html = remove_ads(response.text)
        print(clean_html)
    else:
        print(f"Error loading page: {response.status_code}")

if __name__ == "__main__":
    main()
