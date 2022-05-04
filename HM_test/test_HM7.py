from HM7.all_func_HM7 import check_palindrome
from HM_test import task_HM7
import pytest


@pytest.mark.parametrize("word, exp_result", [("1221", True), (12331, False), (12, False), ("12321", True), (1, True)])
def test_check_palindrome(word, exp_result):
    assert check_palindrome(word) == exp_result


print("\n")


@pytest.mark.parametrize("age", [1, 11, 21, 2, 12, 22, 15, 147, 77, 66, 2.0])
def test_hm7(age):
    task_HM7.hm7_task(age)
