import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="FIREFOX",
        help=(
            "Your options are: FIREFOX CHROME\n "))