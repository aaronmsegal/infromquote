import sys
from bs4 import BeautifulSoup
from urllib2 import urlopen
# import webbrowser

class Entry:
    def __init__(self):
        self.name = None
        self.symbol = None
        self.rank = None
        self.f5link = None
        self.city = None
        self.state = None
        self.industry = None
        self.description = None
        #self.wikiLink = None
        self.ceo = None
        self.website = None
        self.yearlyData = []
    def display(self):
        print self.name
        print self.symbol
        print self.rank
        print self.f5link
        print self.city
        print self.state
        print self.industry
        print self.description
        #print self.wikiLink
        print self.ceo
        print self.website
        for pair in self.yearlyData:
            print pair[0] + " : " +pair[1]
    def toFile(self, writeFile):
        if (not self.name or
            not self.symbol or
            not self.rank or
            not self.f5link or
            not self.city or
            not self.state or
            not self.industry or
            not self.description or
            not self.ceo or
            not self.website or
            not self.yearlyData):
            return
        writeFile.write( u' '.join((self.name, "\n")).encode('utf-8'))
        writeFile.write( u' '.join((self.symbol, "\n")).encode('utf-8'))
        writeFile.write( u' '.join((str(self.rank), "\n")).encode('utf-8'))
        writeFile.write( u' '.join((self.f5link, "\n")).encode('utf-8'))
        writeFile.write( u' '.join((self.city, "\n")).encode('utf-8'))
        writeFile.write( u' '.join((self.state, "\n")).encode('utf-8'))
        writeFile.write( u' '.join((self.industry, "\n")).encode('utf-8'))
        writeFile.write( u' '.join((self.description, "\n")).encode('utf-8'))
        #print self.wikiLink
        writeFile.write( u' '.join((self.ceo, "\n")).encode('utf-8'))
        writeFile.write( u' '.join((self.website, "\n")).encode('utf-8'))
        for pair in self.yearlyData:
            writeFile.write(u' '.join((pair[0], ":", pair[1], "\n")).encode('utf-8'))

def entryFromLin(input):
    entry = Entry()
    data = input.split("\n")

def get_company_basics(file):
    soup = BeautifulSoup(open(file), "lxml")
    companylist = soup.find("div", "company-franchise-result-content")
    entries = []
    for li in companylist.findAll("li"):
        entry = Entry()
        if(li.a):
            name = li.find("span", "company-name")
            if name:
                entry.name = name.string.strip()
            mkdata = li.find("span", "company-list-mkt-data")
            if mkdata:
                entry.symbol = mkdata.string.strip().split(",")[0]
            rank = li.find("span", "ranking")
            if rank:
                entry.rank = int(rank.string.strip()[:-1])
            link = li.a["href"].strip()
            if link:
                entry.f5link = link.strip()
            compInfo_ul = li.find("ul", "company-list-comp-info")
            if compInfo_ul:
                location = compInfo_ul.find("li", "company-location")
                if location:
                    location = location.string.split(",")
                    entry.city = location[0].strip()
                    entry.state = location[1].strip()
                industry = compInfo_ul.find("li", "company-industry")
                if industry:
                    entry.industry = industry.string.strip()
        if(entry.name and entry.rank):
            entries.append(entry)
    return entries

def add_fortune_info(basics):
    for entry in basics:
        print entry.f5link
        html = urlopen(entry.f5link).read()
        soup = BeautifulSoup(html, "lxml")
        company = soup.find("div", "company-franchise-list-item-content")
        if company:
            desc = company.find("div", "company-desc")
            if desc and desc.string:
                entry.description = desc.string.strip()
            data = company.find("div", "company-data")
            if data:
                tables = data.findAll("tbody")
                for i in range(3):
                    for row in tables[i].findAll("tr"):
                        title = row.th.string.strip()
                        value = row.td.string.strip()
                        entry.yearlyData.append([title, value])
                rows = tables[4].findAll("tr")
                entry.ceo = rows[0].td.string.strip()
                entry.website = rows[4].a["href"].strip()
                #entry.display()
    return basics

# BASE_WIKI_URL = "https://en.wikipedia.org/wiki/"
# WIKI_LINKS_FILE = "wikiLinks.txt"
#
# def correct_wiki_links(entries):
#     with open(WIKI_LINKS_FILE, 'w') as target:
#         for entry in entries:
#             entry.wikiLink = BASE_WIKI_URL + entry.name.replace(" ", "_")
#             target.write(entry.wikiLink + "\n")
#             webbrowser.open_new_tab(entry.wikiLink)
#         target.close()
#         raw_input("Ready?")
#     with open(WIKI_LINKS_FILE) as target:
#         for entry in entries:
#             line = target.readline()
#             entry.wikiLink = str(line).strip()
#     return entries
#
# def get_wiki_data(entries):
#     for entry in entries:
#         html = urlopen(entry.wikiLink).read()
#         soup = BeautifulSoup(html, "lxml")
#         table = soup.find("table", "infobox vcard")
#         if not table:
#             entry.wikiLink = entry.wikiLink.replace("_", "")
#             html = urlopen(entry.wikiLink).read()
#             soup = BeautifulSoup(html, "lxml")
#             table = soup.find("table", "infobox vcard")
#         if not table:
#             continue
#         symbolArea = table.find("a", "external text")

DATA_FILE = "500data.txt"

if __name__ == '__main__':
    print 'Argument List:', str(sys.argv)
    entries = get_company_basics(sys.argv[1])
    entries = add_fortune_info(entries)
    with open(DATA_FILE, 'w') as target:
        for entry in entries:
            entry.toFile(target)
            target.write("*$||$*\n")
        target.close()
