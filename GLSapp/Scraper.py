'''
Created on 23/01/2015

@author: dave
'''

import requests
from threading import Thread
from time import sleep

class Scraper(object):
    
    def __init__(self):
        self.pages = []
        self.results = []
        
        self.maxThreads = 10
        self.activeThreads = 0
        self.finishedThreads = 0
        
        self.pattern = ""
        
        print("Scraper initialized")
           
    def addPage(self, url):
        
        print("adding url: " + url)
        
        if not url in self.pages:
            self.pages.append(url)
    
    def addPageList(self, _list):
        for item in _list:
            if not item in self.pages:
                self.pages.append(item)
        
    def run(self, _find, _callFinal):
        if len(self.pages) > 0:
            
            print(self.pages)
            
            self.pattern = _find
            
            print("Starting threaded scraping for " + str(len(self.pages)) + " pages...")
            
            for p in self.pages:
                self.start_scrapeThreads(p, _callFinal)
            
                
        else:
            print("Please add pages to scrape")
        
        return self.results
    
    def start_scrapeThreads(self, _url, _finalFunc):
        if (self.activeThreads >= self.maxThreads):
            sleep(1)
            self.run_scrapeThread(_finalFunc)
        else:
            self.activeThreads += 1
            print("Thread created (" + str(self.activeThreads) + " of "  + str(self.maxThreads) + "... on url: " + _url)
            thread = Thread(target = self.run_scrapeThread, args = (_url, _finalFunc))  
            thread.start()
     
    def run_scrapeThread(self, args):
        page = requests.get(args[0])
        self.__findSearchPattern__(args[0], page)
        self.activeThreads -= 1
        self.finishedThreads += 1
        
        print("Thread finished (" + str(self.finishedThreads) + ") and exiting...")
        self.checkAllThreadsHaveRun(args[1])
        
    def checkAllThreadsHaveRun(self, _finalFunc):
        if self.finishedThreads >= len(self.pages):
            _finalFunc(self.results)
     
    def __findSearchPattern__(self, _url, _page):
        if self.pattern in _page.text:
            print("Bingo! - Added url to results...")
            self.results.append(_url)
        