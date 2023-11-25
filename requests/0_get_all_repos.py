"""Send GET request exercise"""

import requests


def get_repos(url):
    # YOUR CODE HERE
    """Send GET request function"""
    response = requests.get(url, params={'q' : 'webdrivercamp-learning-python'})

    print(f'Response status code: {response.status_code}')
    print(f'Total count of found items: {response.json()['total_count']}')
    res_list = response.json()['items']

    return sorted(res_list, key=lambda x: x['owner']['login'])


if __name__ == "__main__":
    url = "https://api.github.com/search/repositories?q=webdrivercamp-learning-python"

    list_of_items = get_repos(url)
    print()

    for item in list_of_items:
        user = item['owner']['login']
        repo = item['name']

        print(f"{user:15}", repo)
