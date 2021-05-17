import os
import requests
from bs4 import BeautifulSoup
import sys, io
from io import StringIO

# unfinished- currently only prints tag text instead of outputting them to csv files
# some tags are repeated

# alg to extract txt file and place data into csv file
# remember to change the directory path or use relative paths
directory = r'C:\Users\lir6\Desktop\ClearTermsWebScraper\Dev'
for entry in os.scandir(directory):
    if entry.path.endswith(".txt") and entry.is_file():
        with open(entry.path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            # here is the link to handle soup class/id regex
            # https://stackoverflow.com/questions/34660417/beautiful-soup-if-class-contains-or-regex
            for tag in soup.select('div[class*="cont"]'):
                tag_string = tag.get_text().split()
                to_print = ' '.join(tag_string).encode('ascii', errors='replace')
                    # use the following options for the 'errors' argument
                    # ignore, backslashreplace, namereplace, xmlcharrefreplace, replace
                if len(to_print) > 200:
                    print(to_print)
                    print("\n")
                # added heuristic of using tags that contain over 200 characters

# ANOTHER WAY TO LOOP THROUGH FILES IN DIRECTORY
# directory = r'C:\Users\lir6\Desktop\ClearTermsWebScraper\Dev'
# for filename in os.listdir(directory):
#     if filename.endswith(".html"):
#         print(os.path.join(directory, filename))
#     else:
#         continue