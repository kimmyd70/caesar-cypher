from caesar_cypher.caeser_cypher import encrypt, decrypt
from caesar_cypher.caeser_cypher import crack

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

@pytest.mark.skip("pending")
def test_decrypt_sentence():
    actual = decrypt('Yj mqi jxu ruij ev jycui, yj mqi jxu mehij ev jycui.', 16)
    expected = 'It was the best of times, it was the worst of times.'
    assert actual == expected

# 3. Passes -- encryption should handle upper and lower case letters (return w/case match)

@pytest.mark.skip("pending")
def test_encrypt_mixed():
    actual = encrypt('XyZa', 11)
    expected = 'IjKl'
    assert actual == expected
    
# 4. Passes -- encryption should allow non-alpha characters but ignore them, 
# including white space (return same)

@pytest.mark.skip("pending")
def test_encrypt_sentence():
    actual = encrypt('It was the best of times, it was the worst of times.', 16)
    expected = 'Yj mqi jxu ruij ev jycui, yj mqi jxu mehij ev jycui.'
    assert actual == expected
    
# 5. decrypt encrypted version of "It was the best of times, it was the worst 
# of times." WITHOUT knowing the shift used.

# @pytest.mark.skip("pending")
def test_crack_sentence_no_key():
    actual = crack('Yj mqi jxu ruij ev jycui, yj mqi jxu mehij ev jycui.')
    expected = 'Hacking key:  gives It was the best of times, it was the worst of times. Did I do it right?? True'
    assert actual == expected

