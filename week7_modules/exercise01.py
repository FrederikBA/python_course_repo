import requests
import bs4
import selenium


def get_links():
    url = "https://www.cphbusiness.dk/"
    response = requests.get(url)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    links = []
    for link in soup.find_all("a"):
        if (str(link.get("href"))).startswith("https"):
            links.append((link.get("href")))
            
    return links
    

print(get_links())