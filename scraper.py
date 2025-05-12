from newspaper import Article

def fetch_article(url):
    article = Article(url, browser_user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36')
    article.download()
    article.parse()
    return {
        'title': article.title,
        'text': article.text,
        'source': url
    }

def safe_fetch(url):
    try:
        return fetch_article(url)
    except Exception as e:
        print(f"Error fetching article from {url}: {e}")
        return {
            'title': '',
            'text': '',
            'source': url
        }