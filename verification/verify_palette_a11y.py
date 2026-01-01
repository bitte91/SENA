from playwright.sync_api import sync_playwright
import os

def verify_a11y():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local HTML file - using absolute path from current directory
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # Verify labels for "Gerador" inputs
        print("Checking labels...")
        label_size = page.locator("label[for='genSize']")
        label_qty = page.locator("label[for='genQty']")

        assert label_size.is_visible(), "Label for genSize not found"
        assert label_qty.is_visible(), "Label for genQty not found"
        print("Labels found and linked correctly.")

        # Verify toast container attributes
        print("Checking toast container...")
        toast_container = page.locator("#toast-container")
        role = toast_container.get_attribute("role")
        aria_live = toast_container.get_attribute("aria-live")

        assert role == "status", f"Expected role='status', got '{role}'"
        assert aria_live == "polite", f"Expected aria-live='polite', got '{aria_live}'"
        print("Toast container has correct ARIA attributes.")

        # Take a screenshot of the generator form
        page.locator("#tab-gerador").screenshot(path="verification/generator_form_a11y.png")
        print("Screenshot saved to verification/generator_form_a11y.png")

        browser.close()

if __name__ == "__main__":
    verify_a11y()
