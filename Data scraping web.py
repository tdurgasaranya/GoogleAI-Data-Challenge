To extract the data from the URLs  provided,  would need to use a programming language like Python and a web scraping library like BeautifulSoup.
Here's a basic outline of how to achieve this:
1. Install Python and BeautifulSoup:
* **Python:**  Download and install Python from the official website (https://www.python.org/downloads/). 
* **BeautifulSoup:** Install BeautifulSoup using `pip`:  
    ```bash
    pip install beautifulsoup4
    ```
Use code with caution.
2. Write the Code:
from bs4 import BeautifulSoup
import requests

def extract_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find specific elements (adjust these based on the HTML of the webpage)
    # For example, to find a paragraph tag:
    data = soup.find('p').text

    return data

urls = [
    "https://www.kaleida.team/blog/do-tech-layoffs-hurt-women-more",
    "https://365datascience.com/trending/who-was-affected-by-the-2022-2023-tech-layoffs/",
    # ... add other URLs
]

for url in urls:
    data = extract_data(url)
    print(f"Data from {url}: {data}")

Adjust the Code for Each Website:
Inspect the HTML: Use your browser's developer tools to examine the website's HTML structure and find the elements that contain the data you need.
Modify the extract_data function: Adjust the code inside the function to identify the specific elements you need to extract the data points (e.g., soup.find('p'), soup.find('span'), soup.find('div'), etc.)
