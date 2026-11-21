# Task C1 — Code smells in `legacy_invoice.py`

This analysis is based on the original implementation **before refactoring**. `lab6/legacy_invoice.py` is retained unchanged.

| Code smell | Where | Principle / consequence |
|---|---|---|
| Long `if/elif` chain on the student type | Inside the course loop and the international after-loop condition | **OCP:** a new fee category requires editing `make_invoice`. |
| Magic numbers: 1200, 0.5, 2000, 5000 | Fee calculations | **Readability / maintainability:** rates and fees are unnamed and easy to misapply. |
| Multiple unrelated responsibilities | `make_invoice` calculates fees, formats a string, prints it and writes a file | **SRP:** pricing, presentation and persistence are tightly coupled. |
| File writing hardcoded inside pricing logic | The `open`, `write`, `close` calls | **DIP / testability:** invoice generation depends directly on disk I/O rather than an injected writer. |
| Manual resource management | `open` and `close` without `with` | **Resource safety:** exceptions can prevent the file being closed. |
| Unnecessary iteration by course code | `for code in student.courses` | **Simplicity:** prices depend only on the total number of hours; individual course IDs do not matter. |

Refactoring sequence: named fee constants → dedicated pricing policy classes → `POLICIES` lookup → injected file writer → `SiblingPolicy`. The last extension adds one policy class and one dictionary entry; `make_invoice` is not modified.
