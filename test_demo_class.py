import demo
import pytest

class TestAdd:
    def test_add(self):
        for i in range(10):
            assert demo.add(i, 2) == i + 2

    @pytest.mark.parametrize('a, b, expected', [
        (1,1,2), (2,1,3), (3,1,4), (4,1,5), (5,1,6), (6,1,7), (7,1,8), (8,1,9), (9,1,10)]
    )

    def test_with_param(self, a, b, expected):
        assert demo.add(a, b) == expected

    def test_error(self):
        with pytest.raises(demo.MysteryError):
            assert demo.add(99, 1) == 100

