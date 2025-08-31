import pytest
import io
import sys
from pathlib import Path
from rankedleague.rankedleague.cli import main


def test_cli_can_process_file_from_command_line():
    assert callable(main)

    # Capture stdout to check the output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    try:
        main()
        output = captured_output.getvalue()
        assert "League table written to league_table.txt" in output, f"Expected success message, got: {output}"
        
    finally:
        # Restore stdout
        sys.stdout = sys.__stdout__
        captured_output.close()


def test_cli_creates_output_file():
    output_file = Path("league_table.txt")
    if output_file.exists():
        output_file.unlink()

    main()
    assert output_file.exists()
    
    content = output_file.read_text()
    assert "1. Tarantulas, 6 pts" in content
    assert "2. Lions, 5 pts" in content
    assert "3. FC Awesome, 1 pt" in content
    assert "4. Snakes, 1 pt" in content
    assert "5. Grouches, 0 pts" in content
    
    output_file.unlink()

