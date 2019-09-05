Installation:

`pip install -r requirements.txt`

Run tests this way:

`python -m pytest tests/ -v -s`

Tests with coverage report (example):

`python -m pytest tests/test_bank_whitebox.py -v -s --cov=bank --cov-report html`

Flake8 (example):

`flake8 --max-complexity 10 mccabe.py`