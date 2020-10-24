link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_search_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_element_by_css_selector("#add_to_basket_form")
    assert button is not None, "It's not a basket button =("
    print("Found a basket button")
