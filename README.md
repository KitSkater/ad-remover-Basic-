# Ad Remover (Basic)

A simple Python script to fetch a web page and remove common ad elements using `requests` and `BeautifulSoup`.

## Features

- Detects and removes elements with `ad`, `sponsor`, and similar patterns in `id` or `class`.
- CLI-based: enter a URL and get cleaned HTML printed out.

## Requirements

- Python 3.7+
- `beautifulsoup4`
- `requests`
Usage
bash
python ad_remover.py
Then enter a URL (like https://example.com) when prompted.

Note
This only works on static websites (not ones that load content with JavaScript like YouTube or Instagram).
