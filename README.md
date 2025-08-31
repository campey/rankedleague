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
python -m rankedleague.cli --help

## CLI example
python -m rankedleague.cli tests/test_results_example.txt
