# Week 5 - Code Quality Findings

## 1. Static Analysis Results

- Ruff: 1 issue detected.
- Pylint: 15 issues detected.
- Pylint score: 5.16/10.
- Pytest: 9 out of 9 tests passed.

## 2. Findings Table

| Tool | Code | Issue | Occurrences | Proposed Fix |
|---|---|---|---|---|
| Ruff | I001 | Incorrect import formatting | 1 | Organize imports |
| Pylint | C0304 | Missing final newline | 2 | Add final newlines |
| Pylint | C0114 | Missing module docstring | 2 | Add module descriptions |
| Pylint | C0116 | Missing function docstring | 10 | Document each function |
| Pylint | R1720 | Unnecessary elif after raise | 1 | Replace elif with if |

## 3. Additional Code Smells

- Magic numbers: Grade boundaries are hardcoded.
- Repetitive test code: Similar test functions could
  be simplified using parameterized tests.
- Incomplete test coverage: Invalid scores below 0
  and above 100 are not currently tested.

## 4. Hidden Bug

Pending analysis of the original fees.py implementation.

## 5. Conclusion

Although all nine unit tests passed, static analysis
identified several maintainability and formatting issues.
Refactoring should improve code readability and quality
while preserving the expected behavior.
