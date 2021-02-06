from caesar_cypher.caeser_cypher import encrypt, decrypt
import pytest

# Passes all -- 1. encrypt a string with a given shift

@pytest.mark.skip("pending")
def test_encrypt_lower():
    actual = encrypt('abc', 10)
    expected = 'klm'
    assert actual == expected
    
@pytest.mark.skip("pending")
def test_encrypt_wrap():
    actual = encrypt('xyz', 10)
    expected = 'hij'
    assert actual == expected

@pytest.mark.skip("pending")
def test_encrypt_upper():
    actual = encrypt('JKL', 4)
    expected = 'NOP'
    assert actual == expected

@pytest.mark.skip("pending")
def test_encrypt_mixed():
    actual = encrypt('XyZa', 11)
    expected = 'IjKl'
    assert actual == expected
    
@pytest.mark.skip("pending")
def test_encrypt_same():
    actual = encrypt('abc', 26)
    expected = 'abc'
    assert actual == expected

# Passes all -- 2. decrypt a previously encrypted string with the same shift

@pytest.mark.skip("pending")
def test_decrypt_lower():
    actual = decrypt('klm', 10)
    expected = 'abc'
    assert actual == expected
    
@pytest.mark.skip("pending")
def test_decrypt_wrap():
    actual = decrypt('hij', 10)
    expected = 'xyz'
    assert actual == expected

@pytest.mark.skip("pending")
def test_decrypt_upper():
    actual = decrypt('NOP', 4)
    expected = 'JKL'
    assert actual == expected

@pytest.mark.skip("pending")
def test_decrypt_mixed():
    actual = decrypt('IjKl', 11)
    expected = 'XyZa'
    assert actual == expected

@pytest.mark.skip("pending")
def test_decrypt_same():
    actual = decrypt('abc', 26)
    expected = 'abc'
    assert actual == expected
