import csv
import requests
# from bs4 import BeautifulSoup
import sys, io
import urllib.request
# from urllib.request import Request, urllib


# finished - loops through csv file (sample), which contains company website urls
# does a google search of the terms of conditions of those companies
# extracts the html of the webpage and saves is either as an html or txt file
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
with open('./sample.csv', 'r', encoding='utf-8') as _filehandler:
    csv_reader = csv.reader(_filehandler)
    URL = ""

    for row in csv_reader:

        query = "terms and conditions site: " + row[0]
        for j in search(query, tld="co.in", num=1, stop=1, pause=5):
            URL = j
            r = requests.get(URL)
            html_name = row[0] + ".html"
            txt_file_name = row[0] + ".txt"

            	# save as txt
            with open(txt_file_name, 'w', encoding='utf-8') as file:
                file.write(r.text)
                file.close()

            	# save as html
            # with open(html_name, "w", encoding = 'utf-8') as file:
            #     file.write(r.text)
            #     file.close()
                