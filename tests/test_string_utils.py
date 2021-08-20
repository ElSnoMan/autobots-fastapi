import pytest


def repeat(string: str, times: int) -> str:
    return string * times


EXAMPLES = [
    # (string, times, want)
    ("a", 3, "aaa"),
    ("b", 5, "bbbbb"),
    ("c", 2, "cc"),
    ("d", 1, "d"),
    ("e", 0, ""),
]


@pytest.mark.parametrize("string, times, want", EXAMPLES)
def test_repeat(string, times, want):
    got = repeat(string, times)
    assert want == got
