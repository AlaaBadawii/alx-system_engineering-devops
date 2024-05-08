#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers (not active users, total subscribers)
    for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0
    
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyBot/1.0'}

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return int(data.get('data').get('subscribers'))
    else:
        return 0
