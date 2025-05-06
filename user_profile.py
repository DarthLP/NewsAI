def extract_keywords(text):
    # Very basic version — replace with NLP if needed
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    stopwords = {'the', 'and', 'of', 'in', 'is', 'for', 'to', 'with'}
    keywords = [w for w in words if w not in stopwords and len(w) > 3]
    return list(set(keywords))

class UserProfile:
    def __init__(self, interests, format='bullet'):
        self.interests = interests
        self.format = format
        self.history = []