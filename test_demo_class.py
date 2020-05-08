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


def test_fixture(my_fixture):
    assert my_fixture == 42

def test_capsys(capsys):
    print('hello')
    print('bye')
    out, err = capsys.readouterr()
    assert 'bye\n' in out

def test_monkeypatch(monkeypatch):
    def fake_add(a, b):
        return 42
    monkeypatch.setattr(demo, "add", fake_add)
    assert demo.add(2, 3) == 42

def test_tmpdir(tmpdir):
    some_file = tmpdir.join('something.txt')
    some_file.write('{"hello": "world"}')
    result = demo.read_json(str(some_file))
    print(str((some_file)))
    assert result["hello"] == "world"

