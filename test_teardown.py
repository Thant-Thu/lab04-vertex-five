import pytest


@pytest.fixture
def account():
    print("[setup]")
    yield
    print("[teardown]")


def test_first(account):
    assert True


def test_second(account):
    assert True
