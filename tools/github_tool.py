import requests
import os

def search_github_repos(query: str, limit: int = 5):
    token = os.getenv("GITHUB_TOKEN")

    url = "https://api.github.com/search/repositories"
    headers = {
        "Accept": "application/vnd.github+json"
    }

    # Use token if provided and not a dummy placeholder
    if token and not token.startswith("-") and token.strip():
        headers["Authorization"] = f"Bearer {token}"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)

        if response.status_code == 401:
            return {"error": "GitHub authentication failed. Please check your GITHUB_TOKEN."}
        if response.status_code == 403:
            return {"error": "GitHub API rate limit exceeded. Consider providing a valid GITHUB_TOKEN."}

        response.raise_for_status()
        repos = response.json().get("items", [])

        if not repos:
            return {"message": f"No repositories found for query: '{query}'"}

        return [
            {
                "name": r["full_name"],
                "stars": r["stargazers_count"],
                "url": r["html_url"],
                "description": r.get("description") or "No description provided"
            }
            for r in repos
        ]
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch GitHub repositories: {str(e)}"}

