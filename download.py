# download.py
# by Umair Khan

# Imports
import sys
import requests
from bs4 import BeautifulSoup

# Get list of links
links = open(sys.argv[1], "r").read().splitlines()

# Go through each link
for link in links:

    # Get the name of the book
    html = requests.get(link).text
    soup = BeautifulSoup(html, "html.parser")
    name = str(soup.h1)[4:-5].strip()

    # Produce the filename
    name = name.split()
    for i in range(len(name)):
        name[i] = "".join(x for x in name[i] if x.isalnum())
        name[i] = name[i].capitalize()
    name = "".join(name)
    name = name + ".pdf"

    # Get the download link
    code = link.split("/")[-1]
    url = "https://link.springer.com/content/pdf/{}.pdf".format(code)

    # Download and write the file
    print("Downloading {}...".format(name), end = "", flush = True)
    raw_file = requests.get(url)
    open(name, "wb").write(raw_file.content)
    print("finished!", flush = True)