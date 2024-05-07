#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "Gavon/1.0"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after:
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list
