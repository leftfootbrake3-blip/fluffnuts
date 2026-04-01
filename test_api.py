import sqlite3, os, json, urllib.request, urllib.error

db = os.path.join(os.environ['APPDATA'], 'FluffnutsPro', 'fluffnuts.db')
c = sqlite3.connect(db)
key = c.execute("SELECT value FROM settings WHERE key='key_Claude'").fetchone()[0]
model = c.execute("SELECT value FROM settings WHERE key='model_Claude'").fetchone()[0]
c.close()

with open(r'D:\App DEVELOPMENT\FLUFFNUTS PRO\api_test.txt', 'w') as f:
    f.write(f"Key starts: {key[:20]}...\n")
    f.write(f"Model: {model}\n")
    try:
        payload = json.dumps({
            "model": model,
            "max_tokens": 50,
            "system": "You are a test.",
            "messages": [{"role": "user", "content": "Say hello"}]
        }).encode()
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages", data=payload,
            headers={"x-api-key": key, "anthropic-version": "2023-06-01",
                     "content-type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=30) as r:
            resp = json.loads(r.read())
            f.write(f"SUCCESS: {resp['content'][0]['text']}\n")
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        f.write(f"HTTP ERROR {e.code}: {body}\n")
    except Exception as e:
        f.write(f"ERROR: {type(e).__name__}: {e}\n")
