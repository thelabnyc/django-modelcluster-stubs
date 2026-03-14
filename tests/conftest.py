import pytest


@pytest.fixture(autouse=True)
def _django_settings(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DJANGO_SETTINGS_MODULE", "tests.mypy_test_settings")
