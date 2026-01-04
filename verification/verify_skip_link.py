from playwright.sync_api import sync_playwright
import os
import sys

def verify_skip_link():
    file_path = os.path.abspath("index.html")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{file_path}")

        print("Verifying 'Skip to Main Content' link...")

        # 1. Check if the link exists
        skip_link = page.locator("a[href='#main-content']")
        if skip_link.count() == 0:
            print("❌ FAIL: Skip link not found.")
            sys.exit(1)
        else:
            print("✅ PASS: Skip link found.")

        # 2. Check if the target ID exists
        main_content = page.locator("#main-content")
        if main_content.count() == 0:
            print("❌ FAIL: Main content target (#main-content) not found.")
            sys.exit(1)
        else:
            print("✅ PASS: Main content target found.")

        # 3. Check visibility on focus
        # Initially should be hidden (sr-only usually means small size or clipped)
        # We check if it is visually hidden using heuristics or just trust the class logic
        # But we can check if it becomes visible on focus

        skip_link.focus()

        # Take a screenshot to visually verify
        page.screenshot(path="verification/skip_link_focused.png")
        print("📸 Screenshot taken: verification/skip_link_focused.png")

        # Check if it has styles that make it visible (e.g. z-index, top, left)
        # This is a bit loose, but visual inspection via screenshot is key.
        box = skip_link.bounding_box()
        if box['width'] > 1 and box['height'] > 1:
             print(f"✅ PASS: Skip link has dimensions on focus: {box}")
        else:
             print(f"❌ FAIL: Skip link seems hidden even on focus: {box}")
             sys.exit(1)

        browser.close()

if __name__ == "__main__":
    verify_skip_link()
