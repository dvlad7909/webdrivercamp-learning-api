"""Send GET request with Auth"""

import requests


def get_with_auth(url_):
    # YOUR CODE HERE
    """GET with Auth function"""

    header_content = {'Authorization': 'token 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'}
    response = requests.get(url_, headers=header_content)
    print(f'Response status code: {response.status_code}')

    return len(response.json()), response.headers


if __name__ == "__main__":
    url = "https://api.github.com/user/repos"

    num_of_repos, headers = get_with_auth(url)

    print(f"Total Repos: {num_of_repos}")
    print(f"Response headers: {headers}")
