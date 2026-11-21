# ECU SET312 · Lab 6: TDD, BDD & Refactoring

This is a standalone course-registration and invoice exercise. It does **not** change the IFIND application.

## Layout
- `registration.py`: registration rules, 18-hour maximum, duplicate rejection and course drop.
- `tests/test_registration.py`: four required rules plus Task A1 test of dropping an unregistered course.
- `features/registration.feature` and `features/steps/registration_steps.py`: Behave scenarios and steps, including Task B1 course drop.
- `legacy_invoice.py`: original invoice implementation, retained unchanged.
- `invoice.py`: refactored pricing policies, injected writer and 25%-off `SiblingPolicy`.
- `tests/test_invoice_characterization.py`: original fee behavior, fake writer and sibling-discount tests.
- `../docs/lab6/`: coverage result and image, code-smells analysis, TDD process and team-project scenarios.

## Run from `lab6/`

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install pytest pytest-cov behave ruff
python -m pytest -q
python -m pytest --cov=registration --cov-report=term-missing --cov-fail-under=100
python -m behave
python -m ruff check registration.py invoice.py tests features/steps
python -m ruff check --select C901 --config "lint.mccabe.max-complexity=1" invoice.py
```

Local test run: **10 pytest cases passed** and **100% statement coverage** of `registration.py` (20/20). The Behave feature contains **7 executable scenario instances**: three ordinary scenarios, three Scenario Outline rows, and the new drop scenario. The official Behave and Ruff checks are configured in `.github/workflows/lab6.yml`; they were unavailable in the original local execution environment (packages could not be installed there), so consult GitHub Actions for their independent results.

The three IFIND scenarios in `docs/lab6/ifind_scenarios.md` are acceptance criteria for the team's backlog; they are not part of the isolated course-registration Behave suite.
