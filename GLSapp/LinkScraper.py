import re
from urllib.parse import urlparse

from GLSapp.Scraper import Scraper


class LinkScraper(Scraper):

    def __init__(self, callback):
        super().__init__(callback)
        self.base_url = None
        self.link_pattern = re.compile(r'href=["\'](.*?)["\']')
        self.file_pattern = re.compile(r'\.(css|js|txt|jpg|png|gif|swf|pdf|ico)')

    def remove_base_url(self, url):
        return url.replace(self.base_url, '') or '/'

    def add_result(self, url):
        url = self.remove_base_url(url)
        super().add_result(url)

    def add_error(self, url):
        url = self.remove_base_url(url)
        super().add_error(url)

    def set_base_url(self):

        if len(self.pages) > 0:
            uri = urlparse(self.pages[0])
            self.base_url = '{uri.scheme}://{uri.netloc}'.format(uri=uri)

    def can_run(self):

        self.set_base_url()

        if not self.base_url:
            print("Please add an url to crawl")
            return False

        if len(self.pages) > 1:
            all_same_origin = all(map(lambda url: url.startswith(self.base_url), self.pages))
            if not all_same_origin:
                print("Please make sure all the url are from the same origin when using link mode")
                return False

        return super().can_run()

    def __find__(self, _url, _page):

        # Add the current page.
        self.add_result(_url)

        # Look for more links.
        for match in self.link_pattern.findall(_page.text):

            # Ignore files
            if self.file_pattern.search(match):
                continue

            # Add relative links
            if match.startswith('/'):
                url = self.base_url + match
                self.add_page(url)
                continue

            # Add absolute links (i.e ignore externals)
            if match.startswith(self.base_url):
                self.add_page(match)
                continue
