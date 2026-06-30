from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()
from rich import print

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query : str) -> str:
    """Search the web for recent and reliable infrmation on a topic, return titles, URLs, and snippets of the top results"""
    results = tavily.search(query=query, max_results=5)

    return results

    out = []

    for r in results['results']:
        out.append(
            f"{r['title']}\n{r['url']}\n{r['snippet']}\n"
        )
        return "\n".join(out)

# print(web_search.invoke("What is the latest news on AI?"))

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"

# print(scrape_url.invoke("https://stackoverflow.com/questions/74595712/how-to-run-a-python-file-in-visual-studio-code-from-the-terminal"))