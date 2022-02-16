import sys
import pytest
from section_header_numbers import check_headers, HeaderNumbersException


def test_passing():
    check_headers([1, 2, 3, 4], ".")


def test_duplicate_header_numbers():
    numbers = [1, 3, 3, 4]
    with pytest.raises(HeaderNumbersException) as excinfo:
        check_headers(numbers, ".")
    assert excinfo.value.args[0]["message"] == f"Duplicate header numbers: {numbers}"


def test_nonconsecutive_header_numbers():
    numbers = [1, 3, 4]
    with pytest.raises(HeaderNumbersException) as excinfo:
        check_headers(numbers, ".")
    assert (
        excinfo.value.args[0]["message"] == f"Nonconsecutive Header numbers: {numbers}"
    )


def test_header_numbers_not_in_order():
    numbers = [1, 3, 2]
    with pytest.raises(HeaderNumbersException) as excinfo:
        check_headers(numbers, ".")
    assert excinfo.value.args[0]["message"] == f"Header numbers not in order: {numbers}"


def test_empty_list():
    numbers = []
    with pytest.raises(HeaderNumbersException) as excinfo:
        check_headers(numbers, ".")
    assert excinfo.value.args[0]["message"] == "No header numbers found"


def test_filepath_in_exception():
    numbers = [1, 3, 2]
    with pytest.raises(HeaderNumbersException) as excinfo:
        check_headers(numbers, ".")
    assert excinfo.value.args[0]["filepath"] == "."
