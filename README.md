# rankedleague

Example of a league ranking script, building in small steps to show an evolutionary TDD approach exploring the domain.

## Dev Environment

### Setup
To be able to run tests need to setup venv & install deps

1. `python -m venv venv`
2. `.\venv\Scripts\activate`
3. `pip install -r requirements.txt`

### Running Tests
`pytest --cov=rankedleague`

## CLI

### Installation

Install with pip, either

a) in dev mode, which links here and auto-updates:
```
   pip install -e .
```
b) prod install to site-packages
```
   pip install . 
```

### Usage
```
> rankedleague --help

Usage: rankedleague [OPTIONS] INPUT_FILE OUTPUT_FILE

  Processes league results from input_file, generate league table into
  output_file.

  input_file should contain match results in the format: Team A 1, Team B 2

Options:
  --help  Show this message and exit.
```

e.g.
`rankedleague tests/test_results_example.txt league_table.txt`

