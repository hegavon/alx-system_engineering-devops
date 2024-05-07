#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=None, after=None):
    """A function that recursively fetches hot post titles from a subreddit."""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}
    params = {"after": after} if after else {}

    req = requests.get(url, headers=headers, params=params)

    if req.status_code == 200:
        data = req.json().get("data")
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
