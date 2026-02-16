import requests
from bs4 import BeautifulSoup

# URL of news website
url = "https://www.bbc.com/news"

try:
    # Send GET request
    response = requests.get(url)

    # Check status code
    if response.status_code == 200:
        print("Successfully fetched the webpage!")

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all h2 tags (headlines)
        headlines = soup.find_all("h2")

        # Open file to save headlines
        with open("headlines.txt", "w", encoding="utf-8") as file:
            for index, headline in enumerate(headlines, start=1):
                text = headline.get_text().strip()
                if text:
                    file.write(f"{index}. {text}\n")

        print("Headlines saved successfully in headlines.txt")

    else:
        print("Failed to retrieve webpage. Status Code:", response.status_code)

except Exception as e:
    print("An error occurred:", e)


