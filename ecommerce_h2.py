import os
import requests
from bs4 import BeautifulSoup
import sys, io

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

# change this to local directory first
directory = r'C:\Users\lir6\Desktop\ClearTermsWebScraper\Dev'
for entry in os.scandir(directory):
    if entry.path.endswith(".html") and entry.is_file():
        # enter and extract data
        # print(entry.path)
        with open(entry.path, 'r', encoding='utf-8') as file:
            for j in search(entry.path, tld="co.in", num=1, stop=1, pause=5): 
                url = j
                r = requests.get(url)
                soup = BeautifulSoup(r.content, 'html5lib')

                txt_file_name = entry.path + '.txt'
                with open(txt_file_name, 'w', encoding='utf-8') as txt:
                    table = soup.find_all("p")
                    for row in table:
                        txt.write(row.text.encode('utf-8'))
                    txt.close()