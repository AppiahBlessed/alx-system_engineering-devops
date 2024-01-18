
import requests

def recurse(subreddit, hot_list=[], after=None):
    # Base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Headers with a custom User-Agent
    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    # Parameters for the API request, including 'after' for pagination
    params = {'after': after} if after else {}

    try:
        # Make a request to the Reddit API
        response = requests.get(url, headers=headers, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            
            # Extract titles of hot articles and add them to the list
            children = data['data']['children']
            hot_list.extend(post['data']['title'] for post in children)

            # Check if there are more pages (pagination) and recurse
            after = data['data']['after']
            if after:
                recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            # If the subreddit is invalid or an error occurred, return None
            return None
    except Exception as e:
        # Handle any exceptions (e.g., network errors) and return None
        print(f"An error occurred: {e}")
        return None
