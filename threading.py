import threading, requests

urls = [
    "https://www.example.com",
    "https://httpbin.org/get",
    "https://api.github.com"
]

def download(url):
    r = requests.get(url)
    print(f"{url} -> {len(r.text)} bytes")

threads = [threading.Thread(target=download, args=(u,)) for u in urls]
for t in threads: t.start()
for t in threads: t.join()
