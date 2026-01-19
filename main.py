import os
import requests

BASE_URL = "https://test-triwest.fdc.ibm.com"
API_ROOT = "/api/v3/cmp/"

API_KEY = os.environ.get("CMP_API_KEY", "").strip()
if not API_KEY:
    raise SystemExit("Missing CMP_API_KEY env var")

# Pick ONE auth style (depends on how your CMP is configured):
HEADERS = {
    "Accept": "application/json",
    # "Authorization": f"Bearer {API_KEY}",   # common pattern
    "X-API-Key": API_KEY,                    # common pattern
}

def get(path: str, params: dict | None = None):
    url = BASE_URL.rstrip("/") + path
    r = requests.get(url, headers=HEADERS, params=params, timeout=60)
    r.raise_for_status()
    # If the API sometimes returns text/html, still try JSON:
    try:
        return r.json()
    except Exception:
        return {"raw_text": r.text}

if __name__ == "__main__":
    # 1) Discover endpoints from the API root
    root = get(API_ROOT)
    print("API root keys:", list(root.keys())[:15])

    # 2) Call a specific endpoint (example: users)
    users_path = root.get("users", "/api/v3/cmp/users/")
    users = get(users_path)
    print("Users response type:", type(users))
    print(users if isinstance(users, dict) else users[:1])
