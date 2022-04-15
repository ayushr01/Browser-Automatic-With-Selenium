from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError, InvalidAuthorError

driverservice = Service('/Users/ayushrao/chromedriver')
browser = webdriver.Chrome(service=driverservice)

browser.get("http://quotes.toscrape.com/search.aspx")  # We are using the chrome driver here instead of requests
page = QuotesPage(browser)

try:
    print(page.search_for_quotes())

except InvalidTagForAuthorError as error:
    print(error)
except InvalidAuthorError as error:
    print(error)
except Exception:
    print("An unknown error occurred. Please try again.")

"""
Exception is the most standard one and will therefore give any error classes error
I can BaseException here because it is the highest in terms of inheritance 
I still used exception here because most errors are inherited from it and it will trip those errors
"""
