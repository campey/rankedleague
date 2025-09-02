import pytest
import subprocess
import sys
from pathlib import Path
import pkg_resources


def test_rankedleague_command_is_available():
    """Test that the rankedleague command is available after pip install"""
    try:
        result = subprocess.run(['rankedleague', '--help'],
                                capture_output=True, text=True, timeout=10)
        assert result.returncode == 0, f"Command failed: {result.stderr}"
        assert "Usage: rankedleague" in result.stdout  # should show auto generated help text
    except FileNotFoundError:
        pytest.fail("rankedleague command not found")


def test_rankedleague_command_processes_file():
    """Test that the installed command can actually process a file"""
    input_file = "tests/test_results_example.txt"
    output_file = "test_install_output.txt"

    try:
        result = subprocess.run(['rankedleague', input_file, output_file],
                                capture_output=True, text=True, timeout=10)
        
        assert result.returncode == 0, f"Command failed: {result.stderr}"
        assert "League table written to" in result.stdout

        output_path = Path(output_file)
        assert output_path.exists()

        content = output_path.read_text()
        assert "1. Tarantulas, 6 pts" in content
        assert "2. Lions, 5 pts" in content
        assert "3. FC Awesome, 1 pt" in content
        assert "4. Snakes, 1 pt" in content
        assert "5. Grouches, 0 pts" in content

    finally:
        if Path(output_file).exists():
            Path(output_file).unlink()


def test_rankedleague_command_handles_missing_file():
    """Test that the installed command fails if missing input file"""
    result = subprocess.run(['rankedleague', 'nonexistant.txt', 'output.txt'],
                            capture_output=True, text=True, timeout=10)

    assert result.returncode != 0
    assert "File 'nonexistant.txt' does not exist." in result.stderr

