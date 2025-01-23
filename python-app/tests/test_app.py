from app import main
from src.app import app


def test_main():
    assert main() == "Hello, Python!"

