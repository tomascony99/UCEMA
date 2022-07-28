import pytest
from testbook import testbook


# Set up a shared notebook context to speed up tests.
@pytest.fixture(scope='module')
def tb():
    with testbook('../ypf_finance.ipynb', execute=True) as tb:
        yield tb


# Test using function call.
def test_double_array(tb):
    double_array = tb.ref("double_array")
    assert ypf_df.columns == [2, 4, 6]


# Test using code injection.
def test_double_array_inject(tb):
    double_array = tb.ref("double_array")

    tb.inject("""
        data = [1, 2, 3]
    """)
    data = tb.ref("data")

    assert double_array(data) == [2, 4, 6]