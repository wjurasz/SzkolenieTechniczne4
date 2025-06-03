import ray
import requests

ray.init()

URLS = [
    "http://interia.pl",
    "http://wp.pl",
    "http://onet.pl",
    "http://o2.pl",
    "http://tvn24.pl",
    "http://gazeta.pl",
    "http://rmf24.pl",
    "http://bbc.com",
    "http://cnn.com",
    "http://example.com"
]

@ray.remote
def fetch_size(url):
    response = requests.get(url, timeout=5)
    return f"{url} => {len(response.content)} bajtów"


def main():
    tasks = [fetch_size.remote(url) for url in URLS]
    results = ray.get(tasks)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()