import requests

# URL of the webpage to fetch
url = "https://www.example.com"  # mock url taken

def fetch_and_display_webpage(url):
    try:
        # Sending a GET request to the URL
        response = requests.get(url)

        # Checking if the request was successful
        if response.status_code == 200:
            print('Webpage content fetched successfully!\n')
            print(response.text[:2000])  # Displaying the first 2000 characters
        else:
            print(f'Failed to retrieve webpage. Status code: {response.status_code}')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

# Fetch and display the webpage content
fetch_and_display_webpage(url)