import requests
from bs4 import BeautifulSoup


URL = "https://www.brown.edu/Departments/Italian_Studies/dweb/texts/DecShowText.php?myID=d01intro&expand=empty&lang=eng"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

main_text = results.find_all("div", {"id": "text"})
print(main_text)
