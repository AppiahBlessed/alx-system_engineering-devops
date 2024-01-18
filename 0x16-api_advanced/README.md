1. 0. How many subs?
mandatory
Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

Requirements:

Prototype: def number_of_subscribers(subreddit)
If not a valid subreddit, return 0.
NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.



2. Top Ten
mandatory
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

Requirements:

Prototype: def top_ten(subreddit)
If not a valid subreddit, print None.
NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
 data: This is the main dictionary containing the information returned by the Reddit API.
---------------------------------------------------------------------------
data['data']: Accessing the 'data' key within the main dictionary, which contains information about the subreddit.

data['data']['children']: Accessing the 'children' key within the 'data' dictionary. This is a list of posts within the subreddit.

data['data']['children'][i]: Indexing into the list of posts to get the i-th post. i is the loop variable, so this part fetches the information for the current post in the loop.

data['data']['children'][i]['data']: Accessing the 'data' key within the i-th post dictionary. This contains detailed information about the post.

data['data']['children'][i]['data']['title']: Accessing the 'title' key within the 'data' dictionary for the i-th post. This gives the title of the post.

So, in summary, data['data']['children'][i]['data']['title'] is accessing the title of the i-th post in the list of posts returned by the Reddit API.






