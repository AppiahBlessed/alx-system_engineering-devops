#!/usr/bin/env python3
"""This script querries the API for reddit sand returns
    - the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """This function makes a call to a subreddit-API"""
    
    # Get base url
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Get the headers to send to the server as required by Reddit
    header = {'User-Agent': 'UserAgent/1.0'}

    # Try to catch any error
    try:
        # Make request to End point
        response = requests.get(url, headers=header)
        # To check if the subreddit is invalid
        if response:
            if response.status_code == 200:
                # Parse data into python object
                data = response.json()
                # Print the top ten hot titles
                for i in range(10):
                    print(data['data']['children'][i]['data']['title'])
            else:
                return 0
        # Execute if subreddit is fake
        else:
            print("None")
    except Exception as er:
        print(er)
        return 0
