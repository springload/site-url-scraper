from GLSapp.Scraper import Scraper


class ReferenceScraper(Scraper):

    def __init__(self, callback, pattern):
        super().__init__(callback)
        self.pattern = pattern

    def can_run(self):
        if self.pattern:
            return super().can_run()

        else:
            print("Please add a pattern")
            return False

    def __find__(self, _url, _page):
        if self.pattern in _page.text.lower():
            print("Bingo! Pattern '" + self.pattern + "' found - Added url to results...")
            self.results.append(_url)
