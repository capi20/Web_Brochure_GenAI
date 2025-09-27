import requests
from bs4 import BeautifulSoup

class Website:
    """
    Represents a webpage and provides methods to extract text content and links.
    """
    def __init__(self, url: str):
        self.url = url
        self.body = self._fetch_content()
        self.title, self.text, self.links = self._parse_content()

    def _fetch_content(self):
        response = requests.get(self.url)
        return response.content

    def _parse_content(self):
        soup = BeautifulSoup(self.body, 'html.parser')
        title = soup.title.string if soup.title else "No title found"

        # Clean and extract main text content
        if soup.body:
            for tag in soup.body(["script", "style", "img", "input"]):
                tag.decompose()
            text = soup.body.get_text(separator="\n", strip=True)
        else:
            text = ""

        # Extract and filter all links
        links = [link.get('href') for link in soup.find_all('a')]
        valid_links = [link for link in links if link]

        return title, text, valid_links

    def get_contents(self) -> str:
        """
        Returns a formatted string with the title and content of the webpage.
        """
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"
