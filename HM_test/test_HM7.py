from HM7.all_func_HM7 import check_palindrome
from HM7.task_HM7 import hm7_task
import pytest


@pytest.mark.parametrize("word, exp_result", [("1221", True), (12331, False), (12, False), ("12321", True), (1, True)])
def test_check_palindrome(word, exp_result):
    assert check_palindrome(word) == exp_result



@pytest.mark.parametrize("age", [1, 11, 21,  12, 22, 15, 147, 77, 66, 2])
def test_hm7(age):
    hm7_task(age)
