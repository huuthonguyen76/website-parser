import requests
import os

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from loguru import logger
from markdownify import markdownify as md


class BaseParser(ABC):
    html_executor_url: str

    def __init__(self, html_executor_url=os.getenv("HTML_EXECUTOR_URL")):
        self.html_executor_url = html_executor_url

    @abstractmethod
    def parse(self, url: str) -> str:
        pass
