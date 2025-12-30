
import os
from playwright.sync_api import sync_playwright

def verify_frontend():
    file_path = os.path.abspath("index.html")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 800})
        page.goto(f"file://{file_path}")

        # Take screenshot of the default view (Gerador)
        page.screenshot(path="verification/tab_gerador.png")
        print("Screenshot saved: verification/tab_gerador.png")

        # Click Simulador and take screenshot
        page.click("button[data-tab='simulador']")
        page.wait_for_selector("#tab-simulador", state="visible")
        page.screenshot(path="verification/tab_simulador.png")
        print("Screenshot saved: verification/tab_simulador.png")

        # Click Carteira and take screenshot
        page.click("button[data-tab='carteira']")
        page.wait_for_selector("#tab-carteira", state="visible")
        page.screenshot(path="verification/tab_carteira.png")
        print("Screenshot saved: verification/tab_carteira.png")

        # Click Analise and take screenshot
        page.click("button[data-tab='analise']")
        page.wait_for_selector("#tab-analise", state="visible")
        page.screenshot(path="verification/tab_analise.png")
        print("Screenshot saved: verification/tab_analise.png")

        browser.close()

if __name__ == "__main__":
    verify_frontend()
