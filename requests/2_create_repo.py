"""Send POST request to create"""

import requests
from pprint import pprint


def create_repo(url):
    # YOUR CODE HERE
    """create repo POST request"""

    # Use actual token!!!
    header_content = {'Authorization': 'token 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'}
    payload = {
        'name': 'repo-created-with-api',
        'private': True,
        'has_wiki': False
    }

    response = requests.post(url, headers=header_content, json=payload)
    print(f'Response status code: {response.status_code}')

    return response.json()


if __name__ == '__main__':
    url = 'https://api.github.com/user/repos'

    repo = create_repo(url)
    pprint(repo)
