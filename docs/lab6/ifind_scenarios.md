# Part D — Three Gherkin scenarios for IFIND

**Team story:** As an existing IFIND user, I want to log in securely with my email and password so that I can access my account.

Source in this repository: `backend/app/routers/auth.py`, `POST /auth/login`, which returns an access token for valid email-verified credentials, rejects invalid credentials with HTTP 401, and rejects an unverified email with HTTP 401.

```gherkin
Feature: IFIND secure login
  As a registered IFIND user
  I want to log in with my email and password
  So that I can access my account securely

  Scenario: Verified user logs in successfully
    Given an IFIND account with a verified email and a known password
    When the user submits the correct email and password
    Then the login response status is 200
    And the response contains an access token

  Scenario: Incorrect password is refused
    Given an IFIND account with a verified email
    When the user submits the account email and an incorrect password
    Then the login response status is 401
    And the error message is "Invalid email or password"

  Scenario: Unverified email cannot log in
    Given an IFIND account whose email is not verified
    When the user submits the correct email and password
    Then the login response status is 401
    And the error message is "Please verify your email first"
```

These are three testable **acceptance specifications**, not executable Behave step definitions. They should be reviewed against the current team's backlog and implemented in future IFIND integration tests.
