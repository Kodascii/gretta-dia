# Beautiful Soup

```py
from bs4 import BeautifulSoup
```

## Parse HTML Content
- **FROM A LOCAL FILE :**
    ```py
    with open('your_file.html', 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    ```

- **FROM A WEBSITE :**
    ```py
    # $> pip install requests
    import requests

    url = 'https://www.example.com'
    response = requests.get(url)

    # Check for successful response
    if response.status_code == 200:  
        soup = BeautifulSoup(response.content, 'html.parser')
    else:
        print('Error fetching website content')
    ```

## Navigating the HTML Structure:
- **FIND ELEMNTS BY TAG :**
    ```py
    all_paragraphs  = soup.find_all('p')  # Find all paragraphs
    first_paragraph = soup.find('p')      # Find the first paragraph

    for paragraph in all_paragraphs:
        print(paragraph.text)             # Extract text content
    ```

- **FIND ELEMENTS BY NAME :**
    ```py
    specific_class = soup.find('div', class_='my-class')  # Find by class
    specific_id    = soup.find('a', id='unique-id')       # Find by ID
    ```

- **NAVIGATE PARENT-CHILD RELATIONSSHIPS :**
    ```py
    parent_element   = soup.find('div', class_='article')
    child_paragraphs = parent_element.find_all('p')       # Find paragraphs within the div
    ```

- **EXTRACT SPECIFIC DATA :**
    ```py
    title_tag  = soup.find('title')
    title_text = title_tag.string if title_tag else None  # Handle cases where title might be missing

    links = soup.find_all('a')
    for link in links:
        href = link.get('href')  # Get the 'href' attribute value of each link
        print(href)
    ```