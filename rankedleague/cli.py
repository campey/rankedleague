import sys
from .domain import ResultsFile, LeagueTable

def main():
    input_file = "tests/test_results_example.txt"
  
    results_file = ResultsFile(input_file)
    league_table = LeagueTable()
    
    for result in results_file:
        league_table.update_with_result(result)
    
    output_file = "league_table.txt"
    LeagueTable.write_to_file(league_table, output_file)
    print(f"League table written to {output_file}")

if __name__ == '__main__':
    main()
