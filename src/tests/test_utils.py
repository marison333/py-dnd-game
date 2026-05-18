from unittest.mock import patch, mock_open
import pytest
from utils import print_screen


@patch("builtins.print")
@patch("builtins.open", new_callable=mock_open, read_data="TITLE SCREEN")
def test_print_screen(mock_file, mock_print):
    print_screen("fake_file.txt")

    mock_file.assert_called_once_with(
        "fake_file.txt",
        "r",
        encoding="utf-8",
        errors="ignore"
    )
    mock_print.assert_called_once_with("TITLE SCREEN")


def test_print_screen_file_not_found():
    with pytest.raises(FileNotFoundError):
        print_screen("missing_file.txt")