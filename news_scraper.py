import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all(["h1", "h2"])

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for headline in headlines:
            text = headline.get_text(strip=True)
            if text:
                file.write(text + "\n")

    print("Headlines saved successfully!")
else:
    print("Failed to access website")