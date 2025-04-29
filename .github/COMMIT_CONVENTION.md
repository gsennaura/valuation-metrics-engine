# Commit Message Conventions

This project follows a simple and clear commit message convention based on [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

---

## Structure

Each commit message should follow the format:

```
<type>: <short and meaningful description>
```

Example:

```
feat: add calculation logic for market and auction values
fix: correct year fallback when default ratios are missing
docs: update README with setup instructions
```

---

## Allowed Types

| Type  | Meaning |
|:------|:--------|
| feat  | Adding a new feature |
| fix   | Fixing a bug or incorrect behavior |
| docs  | Documentation only changes |
| style | Code style changes (formatting, linting, no logic changes) |
| refactor | Code restructuring without changing behavior |
| test  | Adding or updating tests |
| chore | General maintenance tasks (e.g., updating dependencies, minor build setup changes) |

---

## Examples

- `feat: create EquipmentService with get_equipment_value method`
- `fix: handle ModelNotFoundError gracefully`
- `docs: add overview section to README`
- `test: add unit tests for calculate_equipment_value`
- `chore: update Makefile to include clean command`

---

## Branch Naming Convention

Follow Git Flow style:

```
feature/<feature-name>
fix/<fix-description>
docs/<documentation-update>
chore/<chore-description>
```

Example:

- `feature/implement-equipment-valuation`
- `fix/missing-default-ratio-handling`
- `docs/update-readme-requirements`
- `chore/setup-makefile`

---

## Why This Matters

- Clear commit history
- Easier code reviews
- Better changelog generation (if automated in the future)
- Professional and scalable development workflow