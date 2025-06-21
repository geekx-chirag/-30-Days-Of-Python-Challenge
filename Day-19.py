import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# List of files to download
files = [
    "https://example.com/file1.jpg",
    "https://example.com/file2.jpg",
]

# Directory to save files
os.makedirs("downloads", exist_ok=True)

def download_file(url):
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            file_name = os.path.join("downloads", url.split("/")[-1])
            with open(file_name, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            return f"Downloaded: {file_name}"
        else:
            return f"Failed to download {url}: Status code {response.status_code}"
    except Exception as e:
        return f"Error downloading {url}: {e}"

# Using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as executor:
    future_to_url = {executor.submit(download_file, url): url for url in files}

    for future in as_completed(future_to_url):
        result = future.result()
        print(result)

print("All downloads completed.")
