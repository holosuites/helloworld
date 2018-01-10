from bithacks import bithacks

def test_computeSign():
    if bithacks.computeSign(-42) != -1:
        raise AssertionError
    if bithacks.computeSign(0) != 0:
        raise AssertionError
    if bithacks.computeSign(42) != 1:
        raise AssertionError

def test_detectOppositeSigns():
    if bithacks.detectOppositeSigns(-1,-1):
        raise AssertionError()
    if not bithacks.detectOppositeSigns(-1,1):
        raise AssertionError()
    if not bithacks.detectOppositeSigns(1,-1):
        raise AssertionError()
    if bithacks.detectOppositeSigns(1,1):
        raise AssertionError()
