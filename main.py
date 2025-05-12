from scraper import safe_fetch
from summarizer import summarize_text
from user_profile import UserProfile

user = UserProfile(interests=['economics'])

# Add hardcoded articles for testing
article1 = safe_fetch("https://www.dw.com/en/eu-pledges-500-million-for-science-amid-us-funding-cuts/a-72438165")
article2 = safe_fetch("https://www.reuters.com/science/eus-von-der-leyen-announces-500-mln-euros-package-boost-european-science-2025-05-05/")
article3 = safe_fetch("https://www.theguardian.com/science/2025/may/05/british-scientists-eu-horizon-research-funding-programme")

articles = [a for a in [article1, article2, article3] if a["text"].strip()]

# Summarize the articles
summary = summarize_text(articles, user)

print(summary)
for article in articles:
    print(f"Sources: {article['source']}") 