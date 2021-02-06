from caesar_cypher.caeser_cypher import encrypt

# Passes -- 1. encrypt a string with a given shift

# @pytest.mark.skip("pending")
def test_encrypt_lower():
    actual = encrypt('abc', 10)
    expected = 'klm'
    assert actual == expected
    
# @pytest.mark.skip("pending")
def test_encrypt_wrap():
    actual = encrypt('xyz', 10)
    expected = 'hij'
    assert actual == expected

# @pytest.mark.skip("pending")
def test_encrypt_upper():
    actual = encrypt('JKL', 4)
    expected = 'NOP'
    assert actual == expected

# @pytest.mark.skip("pending")
def test_encrypt_mixed():
    actual = encrypt('XyZa', 11)
    expected = 'IjKl'
    assert actual == expected

# 2. decrypt a previously encrypted string with the same shift
