from HM9.HM9_task2 import get_str_len
import pytest


@pytest.mark.parametrize("word, exp_result", [(1221, type("")),
                                              ([12331, "sds"], type("")),
                                              ({"sd": 123}, type("")),
                                              ((1, 2, 3), type("")),
                                              ({"123"}, type("")),
                                              (123456, type("")),
                                              ])
def test_get_str(word, exp_result):
    assert type(get_str_len(word)) == exp_result

@pytest.mark.parametrize("word, exp_result", [(1221, 4),
                                              ([12331, "sds"], 14),
                                              ({"sd": 123}, 11),
                                              ((1, 2, 3), 9),
                                              ({"123"}, 7),
                                              (123456, 6),
                                              ])
def test_get_len(word, exp_result):
    assert int(get_str_len(word)) == exp_result
