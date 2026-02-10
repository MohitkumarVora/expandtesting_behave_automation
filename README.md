## ExpandTesting Behave Automation

This project is a **Selenium + Behave (BDD)** test automation framework for the demo site `https://practice.expandtesting.com`.  
It uses **page objects**, **Behave step definitions**, and **Allure reports** to provide readable scenarios and rich test reporting.

### 1. Project Overview

- **Test framework**: `behave` (Gherkin-based BDD)
- **Browser automation**: `selenium` with `webdriver-manager`
- **Reporting**: `allure-behave` / Allure HTML reports
- **Pattern**: Page Object Model (POM)

Key flows covered:

- **Login flow** (`login.feature`): valid and invalid login scenarios, URL verification, success/error messages, and logout visibility.
- **Web Inputs flow** (`web_inputs.feature`): entering and validating number/text/password/date fields, rejecting invalid numbers, and verifying the Clear button behavior and output area.

```
EXPANDTESTING_BEHAVE_AUTOMATION
│
├── .idea/                     # IDE configuration (PyCharm)
├── .venv/                     # Python virtual environment
│
├── features/
│   ├── __pycache__/            # Python cache files
│   │
│   ├── configs/                # Configuration files
│   │   └── config_reader.py    # Reads browser, base URL, waits, etc.
│   │
│   ├── pages/                  # Page Object Model (POM) classes
│   │   ├── base_page.py        # Common reusable Selenium actions
│   │   ├── login_page.py       # Login page locators & actions
│   │   └── web_input_page.py   # Web Inputs page locators & actions
│   │
│   ├── steps/                  # Step definition files
│   │   ├── __init__.py
│   │   ├── login_steps.py      # Login feature step definitions
│   │   └── web_input_steps.py  # Web Inputs feature step definitions
│   │
│   ├── __init__.py
│   ├── environment.py          # Behave hooks (before/after scenario)
│   ├── login.feature           # Login feature file
│   └── web_inputs.feature      # Web Inputs feature file
│
├── reports/                    # Allure / test execution reports
│
├── screenshots/                # Failure screenshots
│
├── utils/                      # Utility/helper classes
│   ├── __pycache__/
│   ├── __init__.py
│   ├── driver_factory.py       # Browser driver initialization
│   └── screenshot_utils.py     # Screenshot capture logic
│
├── .gitignore                  # Git ignored files
├── behave.ini                  # Behave configuration (tags, formatters)
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── run.py                      # Test execution entry point
```





### 2. Project Structure

- **`features/`**
  - **`login.feature`**: Scenarios for login functionality.
  - **`web_inputs.feature`**: Scenarios around the “Web inputs” page.
  - **`environment.py`**: Behave hooks:
    - `before_all`: loads config using `ConfigReader`.
    - `before_scenario`: creates a WebDriver via `create_driver()` and navigates to the base URL.
    - `after_step`: on failure, captures a screenshot and attaches it to Allure.
    - `after_scenario`: quits the driver.
  - **`configs/config.ini`**: Central configuration.
    - `[app] base_url` – currently `https://practice.expandtesting.com`
    - `[browser] name` – e.g. `chrome` or `firefox`
    - `[timeouts] explicit_wait` – global explicit wait value.
  - **`configs/config_reader.py`**: Wrapper around `config.ini` for easy access (base URL, browser, timeouts).
  - **`pages/`**
    - `base_page.py`: Common Selenium helpers (click, type, waits, etc.).  
      *(Not shown here, but used as the base for all page objects.)*
    - `login_page.py`: Page object for the Login page (open page, enter username/password, click Login, read messages, check logout button).
    - `web_input_page.py`: Page object for the Web Inputs page (fill form fields, click buttons, read outputs, check cleared values).
  - **`steps/`**
    - `login_steps.py`: Step definitions that bind Gherkin phrases to `LoginPage` actions and assertions.
    - `web_input_steps.py`: Step definitions for the Web Inputs scenarios, including date parsing/normalization.

- **`utils/`**
  - **`driver_factory.py`**: Creates the Selenium WebDriver instance based on config:
    - Supports `chrome` and `firefox`.
    - Uses `webdriver-manager` to download/manage drivers automatically.
    - Applies sensible defaults (incognito/private mode, maximized window, notifications disabled, implicit wait, cookie cleanup).
  - **`screenshot_utils.py`**: Captures screenshots on failure for Allure attachments.

- **`behave.ini`**
  - Configures Behave to use the Allure formatter:
    - `format = allure_behave.formatter:AllureFormatter`
    - `outfiles = reports/allure-results`

- **`run.py`**
  - Helper script to:
    - Optionally clean previous Allure results (via `clean_allure()`).
    - Run the Behave test suite.
    - Generate and open the Allure HTML report in the browser:
      - `allure generate reports/allure-results -o reports/allure-report --clean`
      - `allure open reports/allure-report`

- **`requirements.txt`**
  - Minimal dependencies:
    - `selenium`
    - `behave`
    - `webdriver-manager`
    - `allure-behave`

### 3. Prerequisites

- **Python**: 3.8+ recommended.
- **Browsers**:
  - Google Chrome and/or Mozilla Firefox installed.
- **Allure CLI**:
  - The `run.py` script assumes the `allure` command is available on your system `PATH`.
  - Install it following the official instructions (`allure-commandline`) for your OS.

### 4. Setup Instructions

From the project root (`expandtesting_behave_automation`):

```bash
pip install -r requirements.txt
```

If you use a virtual environment, create and activate it first, then install the requirements.

### 5. Configuration

Main runtime configuration is in `features/configs/config.ini`:

- **Base URL**
  - `[app] base_url = https://practice.expandtesting.com`
  - Change this if your target environment URL differs.

- **Browser selection**
  - `[browser] name = chrome`
  - Supported values (based on `driver_factory.py`):
    - `chrome`
    - `firefox`

- **Timeouts**
  - `[timeouts] explicit_wait = 10`
  - Adjust global explicit wait according to your environment’s performance.

### 6. Running the Tests

#### Option A: Using Behave directly

From the project root:

```bash
behave
```

This:

- Uses `behave.ini` to enable the Allure formatter.
- Writes Allure results into `reports/allure-results`.

You can also run a **single feature** or **tagged scenarios**, for example:

```bash
# Run only login scenarios
behave features/login.feature

# Run only the Inputs feature tagged with @inputs
behave -t @inputs
```

#### Option B: Using `run.py` with Allure report generation

From the project root:

```bash
python run.py
```

This will:

1. Run `behave` (collecting Allure results under `reports/allure-results`).
2. Generate an Allure HTML report in `reports/allure-report`.
3. Open the Allure report in a browser via `allure open`.

> **Note**: Make sure the `allure` CLI is installed and available in your system path, otherwise report generation/opening will fail even if tests pass.

### 7. Writing & Extending Tests

- **Add a new feature**
  - Create a new `.feature` file under `features/` with your Gherkin scenarios.
  - Use descriptive names for features, scenarios, and steps.

- **Create / extend page objects**
  - Add a new page class under `features/pages/` inheriting from `BasePage`.
  - Define locators and reusable actions (clicks, typing, assertions) there instead of in step definitions.

- **Add or modify step definitions**
  - Map new Gherkin steps to Python functions in `features/steps/`.
  - Use the corresponding page object to interact with the UI.

This approach keeps scenarios business-readable while encapsulating technical details in the page objects.

### 8. Troubleshooting

- **Browser does not open / driver issues**
  - Ensure the browser (`chrome`/`firefox`) is installed.
  - Check that your network allows `webdriver-manager` to download drivers.
  - Confirm the browser name in `config.ini` matches what `driver_factory.py` supports.

- **Allure report not generated or not opening**
  - Verify `reports/allure-results` is being populated after a test run.
  - Ensure Allure command-line (`allure`) is installed and on `PATH`.
  - Try manually running:
    ```bash
    allure generate reports/allure-results -o reports/allure-report --clean
    allure open reports/allure-report
    ```

- **Scenarios fail due to URL or message mismatches**
  - Check that the base URL in `config.ini` is still valid and the site has not changed.
  - Validate that locators in page objects (`login_page.py`, `web_input_page.py`) still match the current DOM.

---

If you plan to share this repository, this `README` should give new contributors everything they need to **install dependencies**, **configure the environment**, **run tests**, and **understand the existing coverage**.

