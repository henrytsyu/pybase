from src.main import main


def test_main() -> None:
    result: int = main()
    assert result == 42
