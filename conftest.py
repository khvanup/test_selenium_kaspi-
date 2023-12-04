import pytest

@pytest.fixture()
def set_up():
    print(f"\nНачало этапа")
    yield
    print(f"\nКонец этапа")

@pytest.fixture(scope="module")
def set_group():
    print(f"\nНачало тестирования")
    print("Kaspi.kz".center(18, '-'))

    yield
    print(f"\nКонец тестирования")