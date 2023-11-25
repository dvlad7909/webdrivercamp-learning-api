"""GET the newly created repo"""

import requests


def get_created_repo(url_):
    """GET repo and assert values"""
    # YOUR CODE HERE

    header_content = {'Authorization': 'token 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'}
    response = requests.get(url_, headers=header_content)

    print(f'Response status code: {response.status_code}')
    repo = response.json()

    assert repo['has_wiki'] == False
    assert repo['private'] == True
    assert repo['name'] == 'repo-created-with-api'
    assert repo['owner']['login'] == 'dvlad7909'


if __name__ == "__main__":
    owner = 'dvlad7909'
    repo = 'repo-created-with-api'
    url = f'https://api.github.com/repos/{owner}/{repo}'

    get_created_repo(url)
