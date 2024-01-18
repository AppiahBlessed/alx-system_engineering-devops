#!/usr/bin/python3
"""This script querries the Reddit API and manipulates the datai"""
import requests


def number_of_subscribers(subreddit):
    """Checks number of subscribers"""
    # End point to get the subreddit
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # We set headers as specified by Reddit
    header = {"User-Agent": "UserAgent/1.0"}

    # Try to catch any errors that would happen
    try:
        # Query with headers sent to server
        response = requests.get(url, headers=header, allow_redirects=False)
        # Check if there wasnt any HTTP error
        if response.status_code == 200:
            # Parse data to normal python dictionary
            data = response.json()
            # Number count
            data_returned = data.get("data")
            return data_returned.get("subscribers")
        else:
            return 0
    except Exception as er:
        print(er)
