from playwright.sync_api import sync_playwright
import os

def verify_accessibility():
    file_path = os.path.abspath("index.html")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{file_path}")

        # 1. Verify Grid Accessibility
        print("Verifying Grid Accessibility...")
        ball = page.locator(".ball").first

        # Simulate selection via keyboard (Enter)
        ball.focus()
        page.keyboard.press("Enter")
        page.screenshot(path="verification/grid_accessibility.png")
        print("Grid accessibility screenshot taken.")

        # 2. Verify Wallet Accessibility
        print("\nVerifying Wallet Accessibility...")

        # Add a game manually to populate wallet
        page.reload()
        balls = page.locator(".ball")
        for i in range(6):
            balls.nth(i).click()
        page.get_by_role("button", name="Adic. Manual").click()

        # Switch to Wallet tab
        page.locator("button.nav-tab[data-tab='carteira']").click()

        # Check toolbar buttons
        pdf_btn = page.locator("button[onclick='exportPDF()']")
        print(f"PDF button HTML: {pdf_btn.evaluate('el => el.outerHTML')}")

        page.screenshot(path="verification/wallet_accessibility.png")
        print("Wallet accessibility screenshot taken.")

        browser.close()

if __name__ == "__main__":
    verify_accessibility()
