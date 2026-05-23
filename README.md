# lilalelu
(Not) all your favourite choir warmups in one app - so you can vary them from rehearsal to rehearsal.

**STATUS: Still in development.**

## How to run?
1. Install [Python](https://www.python.org/downloads/) and [venv](https://docs.python.org/3/library/venv.html) (if not already satisfied).
2. Clone the repository: `git clone https://github.com/karlhaensel/lilalelu.git`
3. Create a virtual environment: `python -m venv .venv`
4. Activate the virtual environment:
    - on Linux/ macOS: `source .venv/bn/activate`
    - on Windows(CMD): `.venv\Scripts\activate`
    - on Windows (PowerShell): `.venv\Scripts\Activate.ps1`
5. Install dependencies: `pip install -r requirements.txt`
6. (optional, if you want to contribute) Install pre-commit hooks: `pre-commit install`
7. Run the app: `python -m main.py`