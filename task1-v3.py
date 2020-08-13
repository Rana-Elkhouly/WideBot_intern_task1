import time
import urllib
import bs4
import requests

main_url = "https://en.wikipedia.org/wiki/Special:Random"
visited = []
counter = 0

def find_first_link(url):
    response = requests.get(url)
    data = response.text
    soup = bs4.BeautifulSoup(data, "html.parser")
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    article_link = None
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break
    if not article_link:
        return
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
    return first_link

def philosophy(counter,url):
    counter += 1
    print(counter,url)
    if url == "https://en.wikipedia.org/wiki/Philosophy":
        print("Philosophy page is reached!")
        return 
    if url in visited:
        index = visited.index(url)
        print("Stuck in a loop! Last page is visited before in",index+1,"time")
        return 
    new_link = find_first_link(url)
    if not new_link:
        print("We are in an article without any outgoing Wikilinks!")
        return 
    visited.append(url)
    time.sleep(0.5)
    philosophy(counter,new_link)
    
philosophy(counter,main_url)