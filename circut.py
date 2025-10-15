import pytest
from majority3.core import majority3, majority3_alt, majority3_bitwise

@pytest.mark.parametrize("in1,in2,in3,expected", [
    (False, False, False, False),
    (False, False, True,  False),
    (False, True,  False, False),
    (True,  False, False, False),
    (True,  True,  False, True),
    (True,  False, True,  True),
    (False, True,  True,  True),
    (True,  True,  True,  True),
])
def test_majority3(in1, in2, in3, expected):
    assert majority3(in1, in2, in3) == expected
    assert majority3_alt(in1, in2, in3) == expected
    assert majority3_bitwise(in1, in2, in3) == expected
