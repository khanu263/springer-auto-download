# springer-auto-download

This script is designed to facilitate bulk download of the [free books](https://group.springernature.com/gp/group/media/press-releases/freely-accessible-textbook-initiative-for-educators-and-students/17858180) being offered by Springer during the COVID-19 pandemic. A list of all available books can be accessed via [this](https://docs.google.com/spreadsheets/d/1HzdumNltTj2SHmCv3SRdoub8SvpIEn75fa4Q23x0keU/edit#gid=793911758) spreadsheet.

Given a text file containing line-separated URLs (from the "OpenURL" column in the spreadsheet), this script will go through and download each one as a PDF. Each file will be named according to the title of the book. An example file containing the list of links I used is provided in the repo.

All files will be downloaded to the same directory the script is located in.

### Prerequisites

[Python 3](https://www.python.org/) and [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) from your favorite package / environment manager(s).

### Usage

```
python3 download.py [path to text file]
```
