# Lab 6 process evidence

## Registration TDD (Part A)

The `week-6` Git history intentionally records the following stages separately; RED commits contain failing tests, and GREEN commits add the minimum missing functionality:

1. RED rule 1: register adds hours → GREEN: basic registration.
2. RED rule 2: over-18-hour registration is rejected → GREEN: enforce limit → REFACTOR: introduce `MAX_HOURS`.
3. RED rule 3: duplicate registration is rejected → GREEN: reject duplicates.
4. RED rule 4: a course can be dropped → GREEN: remove the registered course.
5. RED Task A1: dropping an unknown course raises `RegistrationError` → GREEN: add guard.

All RED stages were executed locally and failed for the intended missing behavior. All GREEN stages were rerun locally and passed. See GitHub commits for the actual order.

## Characterization and refactoring (Part C)

1. Original `legacy_invoice.py` was copied into `invoice.py`; the three characterization cases passed first.
2. Named fee constants, extracted fee policies, replaced conditional chains with `POLICIES`, and injected an optional writer, rerunning tests at each stage.
3. Added and passed the fake writer regression test.
4. RED Task C2: sibling discount test failed with missing `sibling` policy.
5. GREEN Task C2: introduced a `SiblingPolicy` returning 75% of the regular fee, registered it in `POLICIES`, and left `make_invoice` unchanged.

## Verified local final results

```text
$ python -m pytest --cov=registration --cov-report=term-missing
collected 10 items
tests/test_invoice_characterization.py .....   [ 50%]
tests/test_registration.py .....                [100%]

Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
registration.py      20      0   100%
-----------------------------------------------
TOTAL                20      0   100%

10 passed in 0.09s
```

The output was recorded in a local Python 3.13.5 environment with pytest 9.0.2 and pytest-cov 7.0.0.

**Verification limit:** `behave` and `ruff` were unavailable locally, and package installation failed due networking restrictions. The GitHub Actions workflow runs those separately; until it completes, do not claim those commands passed.

The PNG coverage image is a **rendering of actual terminal output**, not a photograph of a VS Code terminal window.
