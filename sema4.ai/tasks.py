from robocorp.tasks import task
import time
from robocorp import browser
@task
def open_page():
    page = browser.goto("https://youtube.com/")
    page.wait_for_load_state()

    try:
        accept_button = page.locator("button:has-text('Accept All')")
        accept_button.click()
        print("Clicked 'Accept All' button.")
    except Exception as e:
        print("Could not find 'Accept All' button:", e)

    try:
        page.wait_for_load_state()
        time.sleep(5)
        search_box = page.locator("input#search")
        time.sleep(2)
        search_box.fill("MrRafsan0")
        print("Input typed successfully")
        time.sleep(2)
        search_button = page.locator("button#search-icon-legacy")
        time.sleep(2)
        search_button.click()
        search_button.click()
        print("Search button clicked")
        #browser.goto("https://www.youtube.com/results?search_query=MrRafsan0")
    except Exception as e:
        print("Error interacting with the search elements:", e)
    page.wait_for_load_state()
    time.sleep(5)
    browser.screenshot()