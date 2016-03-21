import sys
from bs4 import BeautifulSoup
from collections import namedtuple

BASE_URL = "http://fortune.com/fortune500/"

def get_company_basics(file):
    #rank name link city state industry
    soup = BeautifulSoup(open(file), "lxml")
    companylist = soup.find("div", "company-franchise-result-content")
    entries = []
    for li in companylist.findAll("li"):
        entry = [None] * 6
        if(li.a):
            name = li.find("span", "company-name")
            if name:
                entry[0] = name.string.strip()
            rank = li.find("span", "ranking")
            if rank:
                entry[1] = int(rank.string.strip()[:-1])
            link = li.a["href"].strip()
            if link:
                entry[2] = link.strip()
            compInfo_ul = li.find("ul", "company-list-comp-info")
            if compInfo_ul:
                location = compInfo_ul.find("li", "company-location")
                if location:
                    location = location.string.split(",")
                    city = location[0].strip()
                    state = location[1].strip()
                    entry[3] = city
                    entry[4] = state
                industry = compInfo_ul.find("li", "company-industry")
                if industry:
                    entry[5] = industry.string.strip()
        if(entry[0]):
            entries.append(entry)
    return entries

if __name__ == '__main__':
    print 'Argument List:', str(sys.argv)
    entries = get_company_basics(sys.argv[1])
    print entries[0][0]
    print entries[0]
    #for line in lines:
    #    print  line
