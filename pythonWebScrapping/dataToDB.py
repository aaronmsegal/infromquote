import sys
import pymysql
import json

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

TABLES = ["companies", "cities", "states", "industries", "yearlyNumbers"]

def getEntries(target):
    entries =  []
    entry = getEntry(target)
    while entry:
        entries.append(entry)
        entry = getEntry(target)
    return entries

def getEntry(target):
    entry = Entry()
    firstLine = target.readline().strip()
    if not firstLine:
        return None
    entry.name = firstLine
    entry.symbol = target.readline().strip()
    entry.rank = target.readline().strip()
    entry.f5link = target.readline().strip()
    entry.city = target.readline().strip()
    entry.state = target.readline().strip()
    entry.industry = target.readline().strip()
    entry.description = target.readline().strip()
    entry.ceo = target.readline().strip()
    entry.website = target.readline().strip()
    pairLine = target.readline().strip()
    while pairLine != "*$||$*" :
        pairs = pairLine.split(":")
        pairs[0] = pairs[0].strip()
        pairs[1] = pairs[1].strip()
        entry.yearlyData.append(pairs)
        pairLine = target.readline().strip()
    #entry.display()
    return entry

def connect():
    try:
        conn = pymysql.connect(
            host='firstdbinstance.cmgttijd34hy.us-east-1.rds.amazonaws.com',
            user='aaronmsegal',
            passwd='',
            database='informquote1',
            autocommit=True)
        return conn
    except Exception as e:
        print 'Failed to open database connection:\n' + str(e)

def dropTables(cur):
    for table in TABLES:
        dropTable(cur, table)

def dropTable(cur, table):
    try:
        sql = "DROP TABLE " + table
        cur.execute(sql)
    except Exception as e:
        print "failed to drop table:\n" + str(e)

def setupTables(cur):
    setupCompanyTable(cur)
    setupCitiesTable(cur)
    setupStatesTable(cur)
    setupIndustriesTable(cur)
    setupYearlyNumbersTable(cur)

def setupCompanyTable(cur):
    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS companies (
        CompanyID int(10) NOT NULL AUTO_INCREMENT,
        Name varchar(50) NOT NULL UNIQUE,
        Symbol varchar(15),
        CityID int(10),
        StateID int(10),
        IndustryID int(10),
        description LONGTEXT,
        CEO varchar(20),
        WebSite varchar(50),
        PRIMARY KEY (CompanyID))''')
    except Exception as e:
        print ('Failed on create companies table:\n' + str(e) )

def setupStatesTable(cur):
    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS states (
        StateID int(10) NOT NULL AUTO_INCREMENT,
        Name varchar(50) NOT NULL UNIQUE,
        PRIMARY KEY (StateID))''')
    except Exception as e:
        print ('Failed on create states table:\n' + str(e) )

def setupCitiesTable(cur):
    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS cities (
        CityID int(10) NOT NULL AUTO_INCREMENT,
        Name varchar(50) NOT NULL UNIQUE,
        PRIMARY KEY (CityID))''')
    except Exception as e:
        print ('Failed on create cities table:\n' + str(e) )

def setupIndustriesTable(cur):
    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS industries (
        IndustryID int(10) NOT NULL AUTO_INCREMENT,
        Name varchar(50) NOT NULL UNIQUE,
        PRIMARY KEY (IndustryID))''')
    except Exception as e:
        print ('Failed on create industries table:\n' + str(e) )

def setupYearlyNumbersTable(cur):
    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS yearlyNumbers (
        EntryID int(10) NOT NULL AUTO_INCREMENT,
        CompanyID int(10) NOT NULL,
        Name varchar(50) NOT NULL,
        Value varchar(15),
        PRIMARY KEY (EntryID))''')
    except Exception as e:
        print ('Failed on create cities table:\n' + str(e) )

def insertData(entry, cur):
    cityId = cityInsert(entry, cur)
    stateId = stateInsert(entry, cur)
    industryId = industryInsert(entry, cur)
    companyId = companyInsert(entry, cityId, stateId, industryId, cur)
    yearlyInsert(entry, companyId, cur)
    #print "inserted:" + entry.name + ", with cid:" + str(companyId)

def yearlyInsert(entry, companyId, cur):
    for pair in entry.yearlyData:
        try:
            sql = '''INSERT INTO yearlyNumbers (
                    CompanyID, Name, Value)
                    VALUES (%s, %s, %s)'''
            record = (companyId, pair[0], pair[1])
            cur.execute(sql, record)
        except Exception as e:
            print ('Failed on yearlyInsert:\n' + str(e) )

def companyInsert(entry, cityId, stateId, industryId, cur):
    # print ("Adding company with cityId:" + str(cityId) +
    #     ", stateId:" + str(stateId) +
    #     ", industryId:" + str(industryId))
    # print "Entry:"
    # entry.display()
    # print "++++++++++++++++++++++++++++++\n"
    try:
        sql = '''INSERT INTO companies (
                name, symbol, cityId, stateId, industryId, description, ceo, website )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
        record = (entry.name, entry.symbol, int(cityId), int(stateId), int(industryId),
                    entry.description, entry.ceo, entry.website)
        cur.execute(sql, record)
        sql = '''SELECT companyId FROM companies
                    WHERE Name = (%s)'''
        record = (entry.name)
        cur.execute(sql, record)
        return cur.fetchone()[0]
    except Exception as e:
        print ('Failed on industryInsert:\n' + str(e) )

def industryInsert(entry, cur):
    try:
        sql = '''SELECT IndustryID FROM industries
                    WHERE Name = (%s)'''
        record = (entry.industry)
        cur.execute(sql, record)
        industryId = cur.fetchone()
        if industryId and industryId[0]:
            #print "exists:id:" + str(industryId[0])
            return industryId[0]
        sql = '''INSERT INTO industries (Name)
                    VALUES (%s)'''
        record = (entry.industry)
        cur.execute(sql, record)
        #print "new entry"
        return industryInsert(entry, cur)
    except Exception as e:
        print ('Failed on industryInsert:\n' + str(e) )

def stateInsert(entry, cur):
    try:
        sql = '''SELECT StateID FROM states
                    WHERE Name = (%s)'''
        record = (entry.state)
        cur.execute(sql, record)
        stateId = cur.fetchone()
        if stateId and stateId[0]:
            #print "exists:id:" + str(stateId[0])
            return stateId[0]
        sql = '''INSERT INTO states (Name)
                    VALUES (%s)'''
        record = (entry.state)
        cur.execute(sql, record)
        #print "new entry"
        return stateInsert(entry, cur)
    except Exception as e:
        print ('Failed on stateInsert:\n' + str(e) )

def cityInsert(entry, cur):
    try:
        sql = '''SELECT CityID FROM cities
                    WHERE Name = (%s)'''
        record = (entry.city)
        cur.execute(sql, record)
        cityId = cur.fetchone()
        if cityId and cityId[0]:
            #print "exists:id:" + str(cityId[0])
            return cityId[0]
        sql = '''INSERT INTO cities (Name)
                    VALUES (%s)'''
        record = (entry.city)
        cur.execute(sql, record)
        #print "new entry"
        return cityInsert(entry, cur)
    except Exception as e:
        print 'Failed on cityInsert:\n' + str(e)

def displayTables(cur):
    for table in TABLES:
        print table + "::"
        displayTable(cur, table)

def displayTable(cur, table):
    try:
        sql = "SELECT * FROM " + table
        cur.execute(sql)
        print cur.fetchall()
    except Exception as e:
        print 'Failed on read ' + table + ':\n' + str(e)

def getSearchJSON(cur):
    try:
        sql = "SELECT CompanyID, Name, Symbol FROM companies"
        cur.execute(sql)
        results = cur.fetchall()
        with open('searchJSON.txt', 'w') as outfile:
            json.dump(results, outfile)
    except Exception as e:
        print 'Failed to create search sjon from companies table + :\n' + str(e)

def entryToJSONFromId(CompanyIDs):
    try:
        sql = '''SELECT companies.CompanyID,
                companies.Name,
                companies.Symbol,
                cities.Name,
                states.Name,
                companies.description,
                companies.CEO,
                companies.Website
                FROM companies
                JOIN cities ON companies.CityID=cities.CityID
                JOIN states ON companies.StateID=states.StateID
                WHERE companies.CompanyID in '''
        sql += str(CompanyIDs)
        cur.execute(sql)
        results = list(cur.fetchall())
        for index in range(len(results)):
            companyList = list(results[index])
            companyID = companyList[0]
            sql = '''SELECT Name, Value
                    FROM yearlyNumbers
                    WHERE CompanyID=%s'''
            cur.execute(sql, companyID)
            companyList.append(cur.fetchall())
            results[index] = companyList
        with open('companyJSON.txt', 'w') as outfile:
            json.dump(results, outfile)
    except Exception as e:
        print 'Failed to create entry json from companies table + :\n' + str(e)


DATA_FILE = "500data.txt"

if __name__ == '__main__':
    with open(DATA_FILE, 'r') as target:
        #entries = getEntries(target)
        target.close()
        #print str(len(entries)) + " Entries found."
        #raw_input("Go?")
        con = connect()
        cur = con.cursor()
        #dropTables(cur)
        #setupTables(cur)
        #for entry in entries:
        #    insertData(entry, cur)
        #print "INSERTS COMPLETE ----------------------------------"
        # displayTables(cur)
        #getSearchJSON(cur)
        entryToJSONFromId((1,2,3,4,5,6,7))
        con.close()
