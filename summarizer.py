import subprocess
import json

def summarize_text(article, user_profile):
    interest_string = ", ".join(user_profile.interests)
    prompt = (
        f"You are a helpful assistant that very shortly summarizes news articles. "
        f"The user is especially interested in: {interest_string}. "
        f"Use the {user_profile.format} format. "
        f"Never make up facts (very important!) Always cite the original source at the end of the summary: \n{article['source']} "
        "Do not change the meaning. Follow user preferences strictly.\n\n"
        f"Summarize the following article:\n{article['text']}"
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