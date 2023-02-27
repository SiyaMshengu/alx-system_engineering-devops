#!/usr/bin/python3
"""Module that consumes the Reddit API and returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'} # Set a custom User-Agent to avoid Too Many Requests errors
    response = requests.get(url, headers=headers, allow_redirects=False) # Do not follow redirects
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
