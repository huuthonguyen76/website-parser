import requests

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from loguru import logger
from markdownify import markdownify as md


class BaseParser(ABC):
    url: str

    def __init__(self, url: str):
        self.url = url

    @abstractmethod
    def parse(self) -> str:
        pass


class StarterStoryParser(BaseParser):
    def parse(self) -> str:
        response = requests.get(self.url)

        soup = BeautifulSoup(response.text, "html.parser")

        article = soup.find('article')
        try:
            # Remove any script tags before processing
            for script in article.find_all('script'):
                script.decompose()

            for element in article.find_all('div', class_='md:hidden'):
                element.decompose()

        except Exception as e:
            logger.error(f"Error parsing article: {e}")

        if article:
            content_for_toc = article.find('div', class_='content-for-toc')

            if content_for_toc:
                markdown_text = md(str(content_for_toc))
                return markdown_text

        return None


if __name__ == "__main__":
    parser = StarterStoryParser("https://www.starterstory.com/stories/the-wayward-home")
    content = parser.parse()

    with open("content.md", "w") as f:
        f.write(content)
