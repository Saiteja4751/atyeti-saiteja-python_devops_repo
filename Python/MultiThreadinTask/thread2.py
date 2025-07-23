import threading
import requests
import os


os.makedirs("downloaded_pages", exist_ok=True)


urls = [
    "https://example.com",
    "https://www.python.org",
    "https://www.wikipedia.org"
]


def download_page(url):
    try:
        response = requests.get(url)
        filename = url.replace("https://", "").replace("www.", "").replace(".", "_") + ".html"
        file_path = os.path.join("downloaded_pages", filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Downloaded: {url} → {file_path}")

    except Exception as e:
        print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    threads = []

    for url in urls:
        t = threading.Thread(target=download_page, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("🏁 All downloads completed.")
