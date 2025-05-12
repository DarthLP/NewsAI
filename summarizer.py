import subprocess
import json

def summarize_text(articles, user_profile):
    interest_string = ", ".join(user_profile.interests)
    combined_text = "\n\n".join(
        f"Source: {article['source']}\nText: {article['text']}" for article in articles
    )
    sources = ", ".join(set(article['source'] for article in articles))

    prompt = (
        f"You are a helpful assistant that summarizes multiple news articles into short bullet points. Combine insights from all sources and keep it really short."
        f"The user is especially interested in: {interest_string}. "
        f"Use the {user_profile.format} format and follow user preferences strictly."
        f"Never make up facts (very important!) and do not change the meaning."
        f"Summarize the following articles:\n{combined_text}"
    )

    result = subprocess.run(
        ['ollama', 'run', 'qwen3:4b'],
        input=prompt.encode('utf-8'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if result.returncode != 0:
        raise RuntimeError(f"Ollama error: {result.stderr.decode()}")

    return result.stdout.decode().strip()