import os
import pytest
import tomllib


def test_uses_local_copy():
    # guards against accidentally testing the stdlib module
    assert os.path.basename(os.path.dirname(tomllib.__file__)) == "tomllib"
    assert "site-packages" not in tomllib.__file__ and "lib/python" not in tomllib.__file__.replace("\\", "/")


def test_basic():
    assert tomllib.loads('a = 1\nb = "x"') == {"a": 1, "b": "x"}


def test_table_and_array():
    assert tomllib.loads('[t]\nx = [1, 2]') == {"t": {"x": [1, 2]}}


def test_invalid():
    with pytest.raises(tomllib.TOMLDecodeError):
        tomllib.loads("a = ")