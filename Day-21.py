import requests
from bs4 import BeautifulSoup

# Step 1: Choose a news site URL
url = "https://www.bbc.com/news" # any site you want 

# Step 2: Fetch the webpage content
response = requests.get(url)

if response.status_code == 200:
    # Step 3: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('h3')
    
    print("Latest Headlines:")
    for idx, headline in enumerate(headlines, 1):
        print(f"{idx}. {headline.get_text(strip=True)}")
else:
    print(f"Failed to fetch the news. Status code: {response.status_code}")