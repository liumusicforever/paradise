# Paradise

## Quick Start

This README provides guidance on setting up and using the Python project, which includes a common logger and a utility to download MP3 files.

1. PYTHON PATH Setup

To ensure that the Python interpreter can find and load the modules of this project correctly, set the PYTHONPATH environment variable to include the directory where your modules are located. This can be done as follows:

On Unix, Linux, macOS:
```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/your/project"
```

2. Using pytest for Testing
To run tests on this project, use the pytest framework. Ensure you have pytest installed, and execute the tests from the root of the project:
```
cd paradise
pytest -s test/
```

3. TDD: Test Driven Development
This project follows the Test Driven Development (TDD) methodology, meaning tests are written before the actual implementation. This approach ensures that code meets its design and behaves as intended.


## Common Objects Introduction
1. `paradise.common.logger`
A configurable logger for logging across different modules.

2. `paradise.common.downloader`
Function to download MP3 files from URLs and save them locally.
