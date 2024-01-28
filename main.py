import requests
from bs4 import BeautifulSoup

def get_top_items(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', class_='item')

    top_items = []
    for item in items:
        title = item.find('h2').text
        price = item.find('span', class_='price').text
        top_items.append((title, price))

    return top_items

def main():
    url = "http://example.com"  # Replace with the actual URL
    top_items = get_top_items(url)
    for item in top_items:
        print(f"Item: {item[0]}, Price: {item[1]}")

if __name__ == "__main__":
    main()