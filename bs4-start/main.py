from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf-8") as html_file:
    soup = BeautifulSoup(html_file, "html.parser")
    print(soup)
    
