#!/usr/bin/env python3

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API returns subscribers for a given subreddit

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        Number of subscribers for subreddit If subreddit is invalid return 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Gavon/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            return data.get("subscribers", 0)
    return 0
