import pytest
import io
import sys
from pathlib import Path
from rankedleague.rankedleague.cli import main


def test_cli_can_process_file_from_command_line():
    assert callable(main)
    
    input_file = "tests/test_results_example.txt"
    output_file = "test_output.txt"
    
    test_output = Path(output_file)
    if test_output.exists():
        test_output.unlink()
    
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    try:
        main.callback(input_file, output_file)
        
        output = captured_output.getvalue()
        assert "League table written to test_output.txt" in output
        
        assert test_output.exists()
        
        content = test_output.read_text()
        assert "1. Tarantulas, 6 pts" in content
        assert "2. Lions, 5 pts" in content
        assert "3. FC Awesome, 1 pt" in content
        assert "4. Snakes, 1 pt" in content
        assert "5. Grouches, 0 pts" in content
        
    finally:
        sys.stdout = sys.__stdout__
        captured_output.close()
        if test_output.exists():
            test_output.unlink()


def test_cli_creates_output_file():
    output_file = Path("league_table.txt")
    if output_file.exists():
        output_file.unlink()

    main.callback("tests/test_results_example.txt", "league_table.txt")
    assert output_file.exists()
    
    content = output_file.read_text()
    assert "1. Tarantulas, 6 pts" in content
    assert "2. Lions, 5 pts" in content
    assert "3. FC Awesome, 1 pt" in content
    assert "4. Snakes, 1 pt" in content
    assert "5. Grouches, 0 pts" in content
    
    output_file.unlink()

