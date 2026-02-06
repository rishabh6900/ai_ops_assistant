import requests
import os

def search_github_repos(query, limit=5):
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise RuntimeError(
            "GITHUB_TOKEN not found. Check your .env file."
        )

    url = "https://api.github.com/search/repositories"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 401:
        raise RuntimeError(
            "GitHub authentication failed (401). "
            "Check if your token is valid and has correct permissions."
        )

    response.raise_for_status()

    repos = response.json().get("items", [])

    return [
        {
            "name": r["full_name"],
            "stars": r["stargazers_count"],
            "url": r["html_url"],
            "description": r["description"]
        }
        for r in repos
    ]
