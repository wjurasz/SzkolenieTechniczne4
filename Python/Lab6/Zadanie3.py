import requests
from multiprocessing import Pool

urls = [
    "http://interia.pl",
    "http://wp.pl",
    "http://onet.pl",
    "http://gazeta.pl",
    "http://o2.pl",
    "http://tvn24.pl",
    "http://polsatnews.pl",
    "http://money.pl",
    "http://rmf24.pl",
    "http://radiozet.pl"
]

def fetch_size(url):
    try:
        response = requests.get(url, timeout=5)
        return (url, len(response.text))
    except Exception as e:
        return (url, f"Error: {e}")

if __name__ == "__main__":
    with Pool(processes=5) as pool: 
        results = pool.map(fetch_size, urls)

    for url, size in results:
        print(f"{url} => {size} bajtów")
