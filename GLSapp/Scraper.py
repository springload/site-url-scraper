'''
Created on 23/01/2015

@author: Dave Cartwright
'''

import requests
from threading import Thread
from time import sleep


class Scraper(object):
    
    def __init__(self):
        self.pages = []
        self.results = []
        
        self.maxThreads = 20
        self.activeThreads = 0
        
        print("Scraper initialized")
    
    # Add a single page
    def addPage(self, url):
        if not url in self.pages:
            print("adding url: " + url)
            self.pages.append(url)
    
    # Add a list of pages
    def addPageList(self, _list):
        for item in _list:
            if not item in self.pages:
                self.pages.append(item)

    def can_run(self):

        if len(self.pages) > 0:
            return True

        else:
            print("Please add pages to scrape")
            return False
    
    # Execute scraper after adding pages
    def run(self, _callFinal):

        if self.can_run():
            print("Starting threaded scraping for " + str(len(self.pages)) + " pages...")
            self.start_scrapeThreads(_callFinal)
        
        return self.results
    
    # Starting point for new thread workers
    def start_scrapeThreads(self, _finalFunc):
        if len(self.pages) == 0:
            self.checkAllThreadsHaveRun(_finalFunc)
            
        elif self.activeThreads >= self.maxThreads:
            sleep(1)
            self.run_scrapeThread(_finalFunc)
            
        else:
            self.activeThreads += 1
            _url = self.pages.pop()
            
            print("Thread created (" + str(len(self.pages)) + ") for url: " + _url)
            
            thread = Thread(target = self.run_scrapeThread, args = (_url, _finalFunc))  
            thread.start()
            
            if self.activeThreads < self.maxThreads:
                self.start_scrapeThreads(_finalFunc)
            
            
    # Method run from with newly started thread  
    def run_scrapeThread(self, _url, _finalFunc):
        try:
            page = requests.get(_url, timeout=5)
            self.__find__(_url, page)
            
        except:
            pass
        
        self.activeThreads -= 1
        self.start_scrapeThreads(_finalFunc)
    
    # Finish scraper if no more url's are left in the list    
    def checkAllThreadsHaveRun(self, _finalFunc):
        if len(self.pages) == 0 and self.activeThreads <= 0:
            _finalFunc(self.results)
        else:
            print("Waiting for " + str(self.activeThreads) + " threads to finish operations...")
    
    #  Private basic pattern search functionality
    def __find__(self, _url, _page):
        raise NotImplementedError()
