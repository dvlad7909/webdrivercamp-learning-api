"""Send PATCH request to update"""

import requests


def update_repo(url_):
    """PATCH function"""
    # YOUR CODE HERE

    header_content = {'Authorization': 'token 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'}
    payload = {
        'description': 'I know Python Requests!'
    }

    response = requests.patch(url_, headers=header_content, json=payload)

    print(f'Response status code: {response.status_code}')
    repo_ = response.json()

    return repo_


if __name__ == '__main__':
    owner = 'dvlad7909'
    repo = 'repo-created-with-api'
    url = f'https://api.github.com/repos/{owner}/{repo}'

    repo = update_repo(url)
    assert repo['description'] == 'I know Python Requests!'
