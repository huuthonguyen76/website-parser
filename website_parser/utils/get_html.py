import requests
import os

from dotenv import load_dotenv

load_dotenv()


def get_html(url: str, html_executor_url: str = os.getenv("HTML_EXECUTOR_URL")):
    if not html_executor_url:
        raise ValueError("HTML_EXECUTOR_URL is not set")

    response = requests.get(
        html_executor_url,
        params={"url": url},
    )

    return str(response.content)


if __name__ == "__main__":
    html = get_html("https://www.starterstory.com/stories/check-your-ielts-essay-online-correction-and-evaluation-service?_kx=Qqdo3eNZ810LLejxM2MVnzUQ2yzuyxgBUACS0WhWGoU.Jchkiv")
    
    with open("test.html", "w+") as f:
        f.write(html)
