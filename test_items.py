#import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_search_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    #test.sleep(30)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button, "It's not a basket button =("
    print("Found a basket button")
