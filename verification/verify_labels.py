from playwright.sync_api import sync_playwright
import os
import sys

def verify_labels():
    file_path = os.path.abspath("index.html")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{file_path}")

        failures = []

        print("Checking 'Números p/ Jogo' label...")
        try:
            # This throws if label is not associated with an input
            el = page.get_by_label("Números p/ Jogo")
            if el.count() == 0:
                failures.append("'Números p/ Jogo' label not associated")
            else:
                print("PASS: 'Números p/ Jogo' label is associated")
        except Exception as e:
            failures.append(f"'Números p/ Jogo' label check failed: {e}")

        print("Checking 'Qtd. Jogos' label...")
        try:
            el = page.get_by_label("Qtd. Jogos")
            if el.count() == 0:
                failures.append("'Qtd. Jogos' label not associated")
            else:
                print("PASS: 'Qtd. Jogos' label is associated")
        except Exception as e:
            failures.append(f"'Qtd. Jogos' label check failed: {e}")

        print("Checking Toast Container ARIA...")
        toast_container = page.locator("#toast-container")
        role = toast_container.get_attribute("role")
        aria_live = toast_container.get_attribute("aria-live")

        if role != "status":
            failures.append(f"Toast container missing role='status' (found: {role})")
        else:
            print("PASS: Toast container has role='status'")

        if aria_live != "polite":
            failures.append(f"Toast container missing aria-live='polite' (found: {aria_live})")
        else:
            print("PASS: Toast container has aria-live='polite'")

        print("Checking Strategy Group Label...")
        strategy_label = page.locator("label:text('Modo do Motor')")
        # Check if the next sibling is a div with role='group'
        # This is a bit specific to the implementation, but let's check if the association exists

        # We want to check if the group has aria-labelledby pointing to this label
        # First we need to find the group container.
        # In current HTML it's a div after the label.

        # Let's try to find the group by its expected accessible name if we were to fix it
        try:
            group = page.get_by_role("group", name="Modo do Motor")
            if group.count() > 0:
                 print("PASS: Strategy buttons are grouped and labeled")
            else:
                 failures.append("Strategy buttons are not in a group with accessible name 'Modo do Motor'")
        except:
             failures.append("Strategy buttons group check failed")


        browser.close()

        if failures:
            print("\nFAILURES:")
            for f in failures:
                print(f"- {f}")
            sys.exit(1)
        else:
            print("\nALL CHECKS PASSED")

if __name__ == "__main__":
    verify_labels()
