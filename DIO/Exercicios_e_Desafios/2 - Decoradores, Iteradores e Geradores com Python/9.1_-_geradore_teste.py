import requests


def fetch_products(api_url, max_pages=10):
    page = 1
    while page <= max_pages:
        response = requests.get(f"{api_url}?page={page}")
        data = response.json()
        for product in data:
            yield product

        if len(data) == 0:
            break

        page += 1


# Uso do gerador
for oneProduct in fetch_products("https://fakestoreapi.com/products"):
    print(oneProduct['title'])
