from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name ():
    assert make_full_name("Jame", "Black-White") == "Black-White; Jame"
    assert make_full_name("Sally", "Davidson") == "Davidson; Sally"
    assert make_full_name("O", "Kh") == "Kh; O"

def test_extract_family_name():
    assert extract_family_name("Black-White; Jame") == "Black-White"
    assert extract_family_name("Davidson; Sally") == "Davidson"
    assert extract_family_name("Kh; O") == "Kh"

def test_extract_given_name():
    assert extract_given_name("Black-White; Jame") == "Jame"
    assert extract_given_name("Davidson; Sally") == "Sally"
    assert extract_given_name("Kh; O") == "O"
    
pytest.main(["-v", "--tb=line", "-rN", __file__])