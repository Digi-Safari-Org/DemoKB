<!-- Create a CONTRIBUTING.md for this repo. Include:
- Branch naming conventions (feature/, fix/, chore/)
- Commit message style (Conventional Commits)
- PR checklist (tests, lint, documentation, security scan)
- Required reviewers and approval rules (codeowners)
- How to run local tests and linters
- How telemetry changes must be reviewed by Security
- How to report security issues privately
Make it suitable for an enterprise team. -->


# Contributing Guidelines

Thank you for contributing to this project! Please follow these guidelines to ensure a smooth and secure development process.

---

## Branch Naming Conventions

- **Features:** `feature/<short-description>`
- **Bug Fixes:** `fix/<short-description>`
- **Chores/Tasks:** `chore/<short-description>`

Example:  
`feature/add-user-auth`  
`fix/order-total-bug`  
`chore/update-dependencies`

---

## Commit Message Style

- Use [Conventional Commits](https://www.conventionalcommits.org/):
  - `feat: add new API endpoint`
  - `fix: correct order calculation`
  - `chore: update dependencies`
  - `docs: update README`
  - `test: add unit tests`
  - `refactor: improve code structure`
- Write clear, concise messages describing the change.

---

## Pull Request Checklist

Before submitting a PR, ensure you have:

- [ ] Added or updated tests for your changes.
- [ ] Run all tests locally and ensured they pass.
- [ ] Run the linter and fixed any issues.
- [ ] Updated documentation as needed.
- [ ] Performed a security scan (if applicable).
- [ ] For telemetry changes, requested a review from the Security team.

---

## Reviewers and Approval Rules

- All PRs must be reviewed and approved by at least one code owner as defined in the `CODEOWNERS` file.
- No PR may be merged without the required approvals.
- Address all reviewer comments and resolve conflicts before merging.

---

## Running Local Tests and Linters

- **Run tests:**  
  ```sh
  pytest