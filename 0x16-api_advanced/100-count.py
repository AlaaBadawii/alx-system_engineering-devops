#!/usr/bin/python3
"""
comment
"""
import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': '100', 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']
        if not articles:  # No more articles
            print_results(count_dict)
            return

        for article in articles:
            title = article['data']['title']
            for word in word_list:
                if word.lower() in title.lower():
                    count_dict[word.lower()] = count_dict.get(word.lower(), 0) + 1

        after = data['data']['after']
        count_words(subreddit, word_list, after, count_dict)
    else:
        print("Failed to retrieve data from Reddit API.")

def print_results(count_dict):
    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")

# Example usage:
count_words("python", ["python", "javascript", "java"])
