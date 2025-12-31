## 2024-10-24 - Grid Accessibility Pattern
**Learning:** Custom interactive grids (like lottery number selectors) often default to `div`s with `onclick`, completely excluding keyboard users.
**Action:** Always add `role="button"`, `tabindex="0"`, and keyboard event handlers (`keydown` for Enter/Space) to these custom controls, along with visible focus states.

## 2024-10-25 - Stateful Toggle Buttons
**Learning:** When using buttons to create a custom "radio group" or mode selector (like the strategy engine), visual styling is not enough for screen readers.
**Action:** Use `aria-pressed` (for toggles) or `role="radio"` (for groups) to communicate state, and ensure the container has `role="group"` and `aria-label`.
