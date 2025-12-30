from playwright.sync_api import sync_playwright

def verify_grid_a11y():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Since it's a static file, we can use file:// protocol.
        # Assuming the file is at /home/jules/index.html (or relative path from cwd)
        import os
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # Wait for grid to render
        page.wait_for_selector("#manualGrid button")

        # 1. Verify buttons exist
        buttons = page.locator("#manualGrid button").all()
        print(f"Found {len(buttons)} buttons")
        assert len(buttons) == 60, "Should have 60 buttons in the grid"

        # 2. Verify button attributes for a specific number (e.g. 10 - Hot)
        # 10 is in STATS.hot (first 5), so it should be Super Quente
        btn_10 = page.locator("#manualGrid button", has_text="10")
        aria_label_10 = btn_10.get_attribute("aria-label")
        print(f"Button 10 aria-label: {aria_label_10}")
        assert "Número 10" in aria_label_10
        assert "Super Quente" in aria_label_10

        # 3. Verify interaction and aria-pressed
        # Initial state
        assert btn_10.get_attribute("aria-pressed") == "false"

        # Click
        btn_10.click()

        # Check selected state
        assert btn_10.get_attribute("aria-pressed") == "true"
        # Check if class updated
        classes = btn_10.get_attribute("class")
        assert "selected" in classes
        print("Interaction test passed: Button 10 selected")

        # 4. Verify a Cold number (e.g. 26 is in cold list)
        btn_26 = page.locator("#manualGrid button", has_text="26")
        aria_label_26 = btn_26.get_attribute("aria-label")
        print(f"Button 26 aria-label: {aria_label_26}")
        assert "Frio" in aria_label_26

        # 5. Take screenshot
        page.screenshot(path="verification/grid_a11y.png")
        print("Screenshot saved to verification/grid_a11y.png")

        browser.close()

if __name__ == "__main__":
    verify_grid_a11y()
