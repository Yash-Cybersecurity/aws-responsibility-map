import re, hashlib, requests
from bs4 import BeautifulSoup
from markdownify import markdownify

HEADERS = {"User-Agent": "aws-responsibility-map/0.1 (+https://github.com/example/aws-responsibility-map)"}

def fetch_html(url: str) -> str:
    r = requests.get(url, headers=HEADERS, timeout=30, allow_redirects=True)
    r.raise_for_status()
    return r.text

def normalize(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
        tag.decompose()
    main = soup.find("main") or soup.find(id="main-content") or soup.body
    text = markdownify(str(main))
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text

def digest(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode()).hexdigest()