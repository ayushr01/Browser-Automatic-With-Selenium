class QuotesPageLocators:
    QUOTE = 'div.quote'
    AUTHOR_DROPDOWN = 'select#author'  # We use hashtag because we are searching by id
    TAG_DROPDOWN = 'select#tag'
    TAG_DROPDOWN_VALUE_OPTION = 'select#tag option[value]'
    SEARCH_BUTTON = 'input[name="submit_button"]'  # We are searching by the attribute name
