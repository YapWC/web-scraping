import requests
from bs4 import BeautifulSoup


class Website:
    def __init__(self, url):
        self.url = url

    def find_contents_with_element(self, element, attribute=None):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        element_contents = soup.find_all(element)
        if attribute==None:
            return [content.text for content in element_contents]
        else:
            return [content.get(attribute) for content in element_contents]
        
class Link:
    def __init__(self, link) -> None:
        self.link = link
    
    def get_response_content(self):
        response = requests.get(self.link)
        content = response.content
        return content