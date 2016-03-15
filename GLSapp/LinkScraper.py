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

    def can_run(self):
        if self.base_url:
            return super().can_run()

        else:
            print("Please add a url")
            return False

    def run(self):

        if len(self.pages) > 0:
            uri = urlparse(self.pages[0])
            self.base_url = '{uri.scheme}://{uri.netloc}'.format(uri=uri)

        super().run()

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
