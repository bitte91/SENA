from playwright.sync_api import sync_playwright
import os

def screenshot_ux():
    file_path = os.path.abspath("index.html")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{file_path}")

        # Ensure we are on the Generator tab (default)
        page.locator("#tab-gerador").wait_for(state="visible")

        # Take a screenshot of the control panel where we made changes
        control_panel = page.locator(".space-y-6").first
        control_panel.screenshot(path="verification/ux_improvements.png")
        print("Screenshot saved to verification/ux_improvements.png")

        browser.close()

if __name__ == "__main__":
    screenshot_ux()
