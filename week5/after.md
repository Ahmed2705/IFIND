# Week 5 - After Refactoring

## 1. Refactoring Changes

### grades.py
- Added module and function docstrings.
- Removed unnecessary elif statements.
- Simplified the control flow.
- Added a final newline.
- Preserved the original grading behavior.

### test_grades.py
- Replaced repetitive test functions with pytest parametrization.
- Corrected import formatting.
- Added module and function docstrings.
- Added a final newline.
- Preserved all nine original test cases.

## 2. Before and After Comparison

| Metric | Before | After |
|---|---|---|
| Ruff issues | 1 | 0 |
| Pylint issues | 15 | 0 |
| Pylint score | 5.16/10 | 10.00/10 |
| Passed tests | 9/9 | 9/9 |

## 3. Final Verification

### Ruff
All checks passed!

### Pylint
Your code has been rated at 10.00/10.

### Pytest
9 passed in 0.05s.

## 4. Refactoring Benefits

- Improved code readability.
- Improved maintainability.
- Reduced code repetition.
- Improved documentation.
- Preserved the behavior covered by the existing tests.

## 5. Fee Calculation Refactoring

Pending completion by the second team member.

## 6. Conclusion

The grading code was successfully refactored without
breaking any existing tests. All static analysis checks
passed, and the Pylint score improved from 5.16 to 10.00.
