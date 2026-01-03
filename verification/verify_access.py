from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine the absolute path to the index.html file
        repo_path = os.getcwd()
        file_url = f"file://{repo_path}/index.html"
        print(f"Navigating to: {file_url}")

        page.goto(file_url)

        # Test 1: Check if "Skip to Content" link exists
        skip_link = page.locator("a[href='#main-content']")
        count = skip_link.count()
        print(f"Skip link found: {count > 0}")

        # Test 2: Check focus behavior (screenshot 1)
        # We need to ensure the link is focused.
        skip_link.focus()
        page.screenshot(path="verification/skip_link_focused.png")
        print("Screenshot taken: skip_link_focused.png")

        # Test 3: Check Tab ARIA roles
        tab_list = page.locator("[role='tablist']")
        print(f"Tablist found: {tab_list.count() > 0}")

        tabs = page.locator("[role='tab']")
        print(f"Tabs found: {tabs.count()}")

        # Test 4: Check aria-selected toggle
        first_tab = tabs.nth(0)
        second_tab = tabs.nth(1)

        sel1 = first_tab.get_attribute('aria-selected')
        sel2 = second_tab.get_attribute('aria-selected')
        print(f"Tab 1 Selected: {sel1}")
        print(f"Tab 2 Selected: {sel2}")

        # Click second tab
        second_tab.click()

        sel1_after = first_tab.get_attribute('aria-selected')
        sel2_after = second_tab.get_attribute('aria-selected')
        print(f"Tab 1 Selected after click: {sel1_after}")
        print(f"Tab 2 Selected after click: {sel2_after}")

        page.screenshot(path="verification/tabs_switched.png")

        browser.close()

if __name__ == "__main__":
    run()
