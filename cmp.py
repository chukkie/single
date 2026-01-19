import os
import json
import ssl
import urllib.request

BASE_URL = "https://test-triwest.fdc.ibm.com"
API_ROOT = "/api/v3/cmp/"

API_KEY = os.environ.get("CMP_API_KEY")
if not API_KEY:
    raise RuntimeError("CMP_API_KEY not set")

headers = {
    "Accept": "application/json",
    "X-API-Key": API_KEY,   # or Authorization: Bearer
}

url = BASE_URL + API_ROOT
req = urllib.request.Request(url, headers=headers)

ctx = ssl.create_default_context()

with urllib.request.urlopen(req, context=ctx) as r:
    body = r.read().decode("utf-8")
    try:
        print(json.dumps(json.loads(body), indent=2))
    except json.JSONDecodeError:
        print(body)
