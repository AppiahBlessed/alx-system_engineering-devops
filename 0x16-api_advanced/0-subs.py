#!/usr/bin/python3
import requests
"""This script querries the Reddit API and manipulates the data
    - Returns the number of subscribers
"""


def number_of_subscribers(subreddit):
    """Checks number of subscribers"""
    # End point to get the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # We set headers as specified by Reddit
    header = {'User-Agent': 'UserAgent/1.0'}

    # Try to catch any errors that would happen
    try:
        # Query with headers sent to server
        response = requests.get(url, headers=header)
        # Check if there wasnt any HTTP error
        if response.status_code == 200:
            # Parse data to normal python dictionary
            data = response.json()
            # Number count
            no_of_subscribers = data['data']['subscribers']
            return no_of_subscribers
        else:
            return 0
    except Exception as er:
        print(er)
        return 0
