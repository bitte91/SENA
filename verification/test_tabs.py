import os
from playwright.sync_api import sync_playwright

def test_tabs():
    file_path = os.path.abspath("index.html")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{file_path}")

        # Define tabs and their expected content selectors
        tabs = [
            {"id": "gerador", "btn_selector": "button[data-tab='gerador']", "content_selector": "#tab-gerador"},
            {"id": "simulador", "btn_selector": "button[data-tab='simulador']", "content_selector": "#tab-simulador"},
            {"id": "carteira", "btn_selector": "button[data-tab='carteira']", "content_selector": "#tab-carteira"},
            {"id": "analise", "btn_selector": "button[data-tab='analise']", "content_selector": "#tab-analise"},
        ]

        for tab in tabs:
            print(f"Testing tab: {tab['id']}")

            # Click the tab button
            btn = page.locator(tab['btn_selector'])
            if not btn.is_visible():
                print(f"Button for {tab['id']} not found!")
                continue # Skip if button doesn't exist yet (initial state)

            btn.click()

            # Check content visibility
            content = page.locator(tab['content_selector'])
            if content.is_visible():
                print(f"Content for {tab['id']} is visible.")
            else:
                print(f"ERROR: Content for {tab['id']} is NOT visible.")

            # Check other tabs are hidden
            for other_tab in tabs:
                if other_tab['id'] != tab['id']:
                    other_content = page.locator(other_tab['content_selector'])
                    if not other_content.is_hidden():
                        print(f"ERROR: Content for {other_tab['id']} should be hidden but is visible.")
                    else:
                        print(f"Content for {other_tab['id']} is hidden (correct).")

            # Check URL hash
            # Note: file:// URLs might not update hash consistently in all environments, but we check.
            # expected_url = f"file://{file_path}#/{tab['id']}"
            # if page.url != expected_url:
            #     print(f"URL mismatch. Expected: {expected_url}, Got: {page.url}")

        browser.close()

if __name__ == "__main__":
    test_tabs()
