'''
Created on 23/01/2015

@author: dave
'''
import sys, getopt, os.path
import csv
from GLSapp.Scraper import Scraper

'''
Main application entry point
''' 
def main():
    
    _scrape = Scraper()
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:f:u", ["help", "file=", "url="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--file"):
            _urlList = readFile(a)
            
            if _urlList:
                _scrape.addPageList(_urlList)

        elif o in ("-u", "--url"):
            _scrape.addPage(a)
    
    results = _scrape.run("<meta")
    
    print(results)
    
'''
Display help
'''
def usage():
    print("Options: /n -h, --help /n --file")
    pass

'''
Read CSV to list object
'''
def readFile(filename):
    
    if os.path.isfile(filename):
    
        csv_list = []
        
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            csv_list = list(reader)
        
        return csv_list
    
    else:
        print("file: "+ filename + " not found")
     
    return False

if __name__ == '__main__':
    main()
    pass