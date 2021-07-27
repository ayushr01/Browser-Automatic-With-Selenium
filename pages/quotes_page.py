from typing import List  # This is just to get support for List in type hiting (line 12)
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

# The following imports are for time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.quote_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> QuoteParser:
        locator = QuotesPageLocators.QUOTE
        quote_tag = self.browser.find_element_by_css_selector(locator)  # This will search just like requests
        return QuoteParser(quote_tag)

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(QuotesPageLocators.AUTHOR_DROPDOWN)
        return Select(element)

    @property
    def tag_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(QuotesPageLocators.TAG_DROPDOWN)
        return Select(element)

    @property
    def search_button(self):
        return self.browser.find_element_by_css_selector(QuotesPageLocators.SEARCH_BUTTON)

    def get_available_authors(self) -> List[str]:
        list = [author.text.strip() for author in self.author_dropdown.options]
        return [item for item in list if item != '----------']

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)
        # This opens the dropdown and selects the option which matches the text we pass

    def get_available_tags(self) -> List[str]:
        list = [tag.text.strip() for tag in self.tag_dropdown.options]  # Options gives us all the options
        # Strip removes spaces and escape sequences
        return [item for item in list if item != '----------']

    def select_tag(self, tag_name: str):
        self.tag_dropdown.select_by_visible_text(tag_name)

    def search_for_quotes(self) -> List[QuoteParser]:
        print("Select one of these authors: [ {} ]".format(" | ".join(self.get_available_authors())))
        author = input("Enter the author you'd like quotes from: ")
        try:
            self.select_author(author)
            # I have not clue what this fucking shit is
            WebDriverWait(self.browser, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, QuotesPageLocators.TAG_DROPDOWN_VALUE_OPTION)
                )
            )
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"Author '{author}' is not an option in the page."
            )
        print("Select one of these tags: [ {} ]".format(" | ".join(self.get_available_tags())))
        tag = input("Enter the tag you want: ")
        try:
            self.select_tag(tag)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"Author '{author}' does not have any quotes tagged with '{tag}'."
            )
        self.search_button.click()
        return self.quotes


class InvalidTagForAuthorError(ValueError):
    pass


class InvalidAuthorError(ValueError):
    pass
