#!/usr/bin/env python3

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    A route that returns recurse
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Gavon/1.0"}

    params = {"after": after} if after else {}

    req = requests.get(url, headers=headers, params=params)

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)

        after = req.json().get("data").get("after")
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
