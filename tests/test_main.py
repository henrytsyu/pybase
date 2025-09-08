from fastapi import FastAPI

from app.main import app


def test_main() -> None:
    assert isinstance(app, FastAPI)
