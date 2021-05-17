import os
import requests
from bs4 import BeautifulSoup
import sys, io
from html.parser import HTMLParser

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 


# alg to extract html file data and convert into txt file
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
                # print("gone into " + entry.path)

                txt_file_name = entry.path + '.txt'
                with open(txt_file_name, 'w', encoding='utf-8') as txt:
                    table = soup.find_all("p")
                    for row in table:
                        txt.write(row.text.encode('utf-8'))
                    txt.close()

                # table = soup.find_all("p")  
                # for row in table:
                    # print(row)
                #     tag = {}
                #     tag['content'] = row.text.encode('utf-8')
                #     p_tag.append(tag)

                # for tag in p_tag:
                #     w.writerow(tag)

            # with open(txt_file_name, 'w', encoding='utf-8') as file:
            #     file.write(r.text)
                # file.close()

# ANOTHER WAY TO LOOP THROUGH FILES IN DIRECTORY
# directory = r'C:\Users\lir6\Desktop\ClearTermsWebScraper\Dev'
# for filename in os.listdir(directory):
#     if filename.endswith(".html"):
#         print(os.path.join(directory, filename))
#     else:
#         continue