# rankedleague

Example of a league ranking script, building in small steps to show an evolutionary TDD approach exploring the domain.

## Setup
To be able to run tests need to setup venv & install deps

python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

## Running Tests
pytest --cov=rankedleague

## CLI help
Install with pip, either
a) in dev mode, which links here and auto-updates:
   pip install -e .
b) prod install to site-packages
   pip install . 

rankedleague --help
rankedleague tests/test_results_example.txt league_table.txt


