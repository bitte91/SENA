
import os
from playwright.sync_api import sync_playwright

def verify_mobile():
    file_path = os.path.abspath("index.html")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Mobile view
        page = browser.new_page(viewport={"width": 375, "height": 667})
        page.goto(f"file://{file_path}")

        # Screenshot Mobile Home
        page.screenshot(path="verification/mobile_home.png")
        print("Screenshot saved: verification/mobile_home.png")

        # Click Simulador on Mobile Bottom Nav
        page.click("button.mobile-nav-item[data-tab='simulador']")
        page.wait_for_selector("#tab-simulador", state="visible")
        page.screenshot(path="verification/mobile_simulador.png")
        print("Screenshot saved: verification/mobile_simulador.png")

        browser.close()

if __name__ == "__main__":
    verify_mobile()
