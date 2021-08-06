# Python FastAPI Course by Autobots from QA at the Point

by Daniel Floyd (@gleekzorp) 😎

## Setup

💡 Use `Poetry` as the package manager to take advantage of the `pyproject.toml` at the Workspace Root

> ⚠️ Python version 3.9 or higher is required

1. Clone this repo and open it in your favorite editor (VS Code, Pycharm, etc)

2. Open the Integrated Terminal and use Poetry to install all dependencies

    ```bash
    # this also creates the virtual environment automatically
    poetry install
    ```

3. Configure your IDE
    - Select Interpreter - Gives you autocomplete, intellisense, etc
    - Configure Tests - We use `pytest` instead of the default `unittest` library
    - Any other settings like Formatter (`black`) and Linter (`flake8`)

4. That's it! Run the tests to see it all work

    ```bash
    poetry run pytest tests
    ```
