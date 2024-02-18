from bs4 import BeautifulSoup as bs
import requests

responce = requests.get("https://qna.habr.com/q/484393")
soup = bs(responce.text, "html.parser")
all_as = soup.find_all('a', href=True)
links = []



choice = input("Output to terminal or save to file ? t/f")
if choice == "t":
    for a in all_as:
        if "https://" in a['href']:
            links.append((a['href']))
    for link in links:
        print(link)
        responce = requests.get(link)
        soup = bs(responce.text, "html.parser")
        all_sub_as = soup.find_all('a', href=True)
        for sub_a in all_sub_as:
            if "https://" in sub_a['href']:
                print(sub_a)
else:
    for a in all_as:
        if "https://" in a['href']:
            links.append((a['href']))
    with open('links.txt', 'w') as file:
        for link in links:
            file.write(link)
            responce = requests.get(link)
            soup = bs(responce.text, "html.parser")
            all_sub_as = soup.find_all('a', href=True)
            for sub_a in all_sub_as:
                if "https://" in sub_a['href']:
                    file.write(sub_a['href'])






