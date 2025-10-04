# E2E E-commerce Test Automation Project

This project is a complete End-to-End test automation suite for the e-commerce website [https://www.saucedemo.com/](https://www.saucedemo.com/).

It is built with Python and Selenium WebDriver and demonstrates a professional automation structure using the Page Object Model (POM).

---

## Key Features

- **Page Object Model (POM):** For clean, maintainable, and reusable code.
- **Data-Driven Testing:** Login tests are driven by data from a CSV file, allowing for easy expansion of test cases.
- **Cross-Browser Support:** Scripts are configured to run on both Chrome and Firefox.
- **End-to-End User Journey:** Automates the full e-commerce flow from login to purchase confirmation.

---

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/BlockAce01/e2e-Test_Automation.git
    cd e2e-Test_Automation
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## How to Run the Tests

You can run the tests directly from the command line from the root project directory.

- **To run the data-driven login tests:**
  ```bash
  python tests/test_login_data_driven.py
    ```

- **To run the End-to-End flow tests:**
  ```bash
  python tests/test_e2e_full_flow.py
    ```