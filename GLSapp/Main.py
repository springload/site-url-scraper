'''
Created on 23/01/2015

@author: dave
'''

import sys, getopt, os.path
import csv
from GLSapp.Scraper import Scraper

# Application handling class
class MainApp():

    def __init__(self):
        self.scraper = Scraper()
        self.pattern = ""

        self.fileUpdated = False

    # Main application entry point
    def main(self):

        try:
            opts, args = getopt.getopt(sys.argv[1:], "h:f:u:p:", ["help", "file=", "url=", "pattern="])
        except getopt.GetoptError as err:
            # print help information and exit:
            print(err) # will print something like "option -a not recognized"
            self.usage()
            sys.exit(2)

        for o, a in opts:
            if o in ("-h", "--help"):
                self.usage()
                sys.exit()

            if o in ("-p", "--pattern"):
                self.pattern = str(a)

            elif o in ("-f", "--file"):
                _urlList = self.readFile(a)
                if len(_urlList) > 0:
                    self.scraper.addPageList(_urlList)

            elif o in ("-u", "--url"):
                self.scraper.addPage(a)

        if (len(self.pattern) <= 0):
            self.usage()
            sys.exit()

        self.scraper.run(self.pattern, self.writeCSV)

    # Write output into file
    def writeCSV(self, _results):
        if self.fileUpdated == False:
            self.fileUpdated = True

            fh = open("Results.txt", "w")
            fh.write('\n'.join(_results) + '\n')
            fh.close()

            print("Result written!")


    # Display help message
    def usage(self):
        print("Options:")
        print("help: -h, --help")
        print("file: -f, --file")
        print("single url: -u, --url")
        print("search pattern: -p, --pattern")
        pass

    # Read list from CSV file
    def readFile(self, _filename):

        if os.path.isfile(_filename):
            csv_list = []
            with open(_filename, 'r') as f:
                reader = csv.reader(f)
                for line in reader:
                    if ("http" in line[0]):
                        csv_list.append(line[0])

            return csv_list

        else:
            print("File: "+ _filename + " not found")

        return False

# Run application from self
if __name__ == '__main__':
    _app = MainApp()
    _app.main()
