import requests
import re
from bs4 import BeautifulSoup

def clean_story(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="container")
    main_text = results.find_all("p")

    full_story = ""
    for element in main_text:
        clean_element = element.text.strip()
        clean_element = re.sub(r'[0-9]+', '', clean_element)
        clean_element = re.sub(r'\[|\]', '', clean_element)
        full_story += clean_element
    return full_story

def return_URL(day, story):
    if (story < 10):
        story = f"0{story}"
    if (day < 10):
        day = f"0{day}"
    URL = f"https://www.brown.edu/Departments/Italian_Studies/dweb/texts/DecShowText.php?myID=nov{day}{story}&lang=eng"
    return URL

print(return_URL(1, 1))