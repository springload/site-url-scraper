'''
Created on 23/01/2015

@author: dave
'''

import requests

class Scraper(object):
    
    def __init__(self):
        self.pages = []
        self.results = []
        
        print("Scraper initialized")
           
    def addPage(self, url):
        
        print("adding url: " + url)
        
        if not url in self.pages:
            self.pages.append(url)
    
    def addPageList(self, _list):
        self.pages + list(set(_list) - set(self.pages))
        
    def run(self, _find):
        if len(self.pages) > 0:
            print(self.pages)
            
            i = 1
            for p in self.pages:
                print("Scraping " + str(i) + " of " + str(len(self.pages)) + ": " + p)
                page = requests.get(p)
                i += 1
                self.__findSearchPattern__(p, page, _find)
                
        else:
            print("Please add pages to scrape")
        
        return self.results
     
    def __findSearchPattern__(self, _url, _page, _pattern):
        if _pattern in _page.text:
            print("Bingo! - Added url to results...")
            self.results.append(_url)
        