#!/usr/bin/env python3

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    A function that recursively fetches hot post titles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store hot post titles.
        after (str): The "after" token for pagination.

    Returns:
        list: A list containing hot post titles from the subreddit.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Gavon/1.0"}

    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            children = data.get("children")
            for child in children:
                title = child.get("data").get("title")
                hot_list.append(title)
            after = data.get("after")
            if after is None:
                return hot_list
            else:
                return recurse(subreddit, hot_list, after)

    return None
