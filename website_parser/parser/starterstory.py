import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from loguru import logger

from base import BaseParser


class StarterStoryParser(BaseParser):
    def parse(self, url: str) -> str:
        response = requests.get(url)

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
    parser = StarterStoryParser()
    content = parser.parse("https://www.starterstory.com/stories/the-wayward-home")

    with open("content.md", "w") as f:
        f.write(content)
