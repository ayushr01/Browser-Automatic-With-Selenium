from locators.quote_locators import QuoteLocators

class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'{self.content} by {self.author}'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.find_element_by_css_selector(locator).text
        # Here it is just element since we want one
        # We use text instead of string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def tag(self):
        locator = QuoteLocators.TAGS
        return self.parent.find_elements_by_css_selector(locator).text # We use elements because it has more than one result in the page
 