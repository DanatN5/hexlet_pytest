from pathlib import Path
from hexlet_pytest.example import reverse


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_reverse():
    before_html = read_file("before.html")
    expected = read_file("result.txt")
    actual = reverse(before_html)

    assert actual == expected