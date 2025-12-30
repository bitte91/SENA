## 2024-10-24 - Grid Accessibility Pattern
**Learning:** Custom interactive grids (like lottery number selectors) often default to `div`s with `onclick`, completely excluding keyboard users.
**Action:** Always add `role="button"`, `tabindex="0"`, and keyboard event handlers (`keydown` for Enter/Space) to these custom controls, along with visible focus states.
