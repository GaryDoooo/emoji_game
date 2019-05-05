from bs4 import BeautifulSoup
import re
import requests

def get_joke():
    url = "https://icanhazdadjoke.com/"
    reading = requests.get(url)
    soup = BeautifulSoup(reading.text, "lxml")
    # print(reading.text)
    spans = soup.find_all('div', {'class': "card-content"})
    # print(spans)
    return spans[0].find("p").get_text()
    # re.sub('[^a-zA-Z]+', '', spans[0].find("p").get_text())
    # for s in spans:
    #    print(s.get_text())
    
    
def main():
    print(get_joke())


if __name__ == "__main__":
    main()