"""
Created on 23/01/2015

@author: Dave Cartwright
"""

import requests
from threading import Thread
from time import sleep


class Scraper(object):

    def __init__(self, callback):
        self.pages = list()
        self.visited_pages = set()
        self.results = list()
        
        self.maxThreads = 20
        self.activeThreads = 0

        self.callback = callback

        print("Scraper initialized")

    # Add a single page
    def add_page(self, url):
        if url not in self.pages and url not in self.visited_pages:
            print("Adding url: " + url)
            self.pages.append(url)

    # Add a list of pages
    def add_page_list(self, _list):
        for url in _list:
            self.add_page(url)

    # Add results
    def add_result(self, url):
        if url not in self.results:
            self.results.append(url)

    # Check if the scraper can run
    def can_run(self):

        if len(self.pages) > 0:
            return True

        else:
            print("Please add pages to scrape")
            return False
    
    # Execute scraper after adding pages
    def run(self):

        if self.can_run():
            print("Starting threaded scraping for " + str(len(self.pages)) + " pages...")
            self.start_scrape_threads()

        return self.results

    # Starting point for new thread workers
    def start_scrape_threads(self):
        if len(self.pages) == 0:
            self.check_all_threads_have_run()

        elif self.activeThreads >= self.maxThreads:
            sleep(1)
            self.run_scrape_thread()

        else:
            self.activeThreads += 1
            _url = self.pages.pop()

            print("Thread created (" + str(len(self.pages)) + ") for url: " + _url)

            thread = Thread(target=self.run_scrape_thread, args=(_url,))
            thread.start()

            if self.activeThreads < self.maxThreads:
                self.start_scrape_threads()

    # Method run from with newly started thread
    def run_scrape_thread(self, _url):
        try:
            page = requests.get(_url, timeout=5)
            self.visited_pages.add(_url)
            self.__find__(_url, page)

        except:
            pass

        self.activeThreads -= 1
        self.start_scrape_threads()
    
    # Finish scraper if no more url's are left in the list    
    def check_all_threads_have_run(self):
        if len(self.pages) == 0 and self.activeThreads <= 0:
            self.callback(self.results)

        else:
            print("Waiting for " + str(self.activeThreads) + " threads to finish operations...")

    #  Private basic pattern search functionality
    def __find__(self, _url, _page):
        raise NotImplementedError()
