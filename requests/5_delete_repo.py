"""Send DELETE request"""

import requests


def delete_repo(url_):
    """DELETE function"""
    # YOUR CODE HERE

    header_content = {'Authorization': 'token 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'}

    response = requests.delete(url_, headers=header_content)

    print(f'Response status code: {response.status_code}')


if __name__ == "__main__":
    owner = 'dvlad7909'
    repo = 'repo-created-with-api'
    url = f'https://api.github.com/repos/{owner}/{repo}'

    delete_repo(url)
