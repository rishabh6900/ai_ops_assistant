import requests
import os

def search_github_repos(query, limit=5):
    url = "https://api.github.com/search/repositories"
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"
    }
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    repos = response.json()["items"]
    return [
        {
            "name": r["full_name"],
            "stars": r["stargazers_count"],
            "url": r["html_url"],
            "description": r["description"]
        }
        for r in repos
    ]
