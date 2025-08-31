import sys
import click
from .domain import ResultsFile, LeagueTable


@click.command()
@click.argument('input_file', type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.argument('output_file', type=click.Path(file_okay=True, dir_okay=False))
def main(input_file, output_file):
    """Processes league results from input_file, generate league table into output_file.
    
    input_file should contain match results in the format:
    Team A 1, Team B 2
    """
    try:
        results_file = ResultsFile(input_file)
        league_table = LeagueTable()
        
        for result in results_file:
            league_table.update_with_result(result)
        
        LeagueTable.write_to_file(league_table, output_file)
        click.echo(f"League table written to {output_file}")
        
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
