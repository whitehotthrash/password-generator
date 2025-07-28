import string
from password_generator import PasswordGenerator

def test_length():
    gen = PasswordGenerator()
    pwd = gen.generate_password(length=8)
    assert len(pwd) == 8
  
def test_no_digits():
    gen = PasswordGenerator()
    pwd = gen.generate_password(use_digits=False)
    assert not any(c.isdigit() for c in pwd)
  
def test_no_symbols():
    gen = PasswordGenerator()
    pwd = gen.generate_password(use_symbols=False)
    assert not any(c in string.punctuation for c in pwd)
  
def test_no_lower():
    gen = PasswordGenerator()
    pwd = gen.generate_password(use_lower=False)
    assert not any(c.islower() for c in pwd)
  
def test_no_upper():
    gen = PasswordGenerator()
    pwd = gen.generate_password(use_upper=False)
    assert not any(c.isupper() for c in pwd)
  
def test_no_lower_and_upper():
    gen = PasswordGenerator()
    pwd = gen.generate_password(use_lower=False, use_upper=False)
    assert not any(c.islower() for c in pwd)
    assert not any(c.isupper() for c in pwd)
  
def test_no_digits_and_symbols():
    gen = PasswordGenerator()
    pwd = gen.generate_password(use_digits=False, use_symbols=False)
    assert not any(c.isdigit() for c in pwd)
    assert not any(c in string.punctuation for c in pwd)
  
def test_no_lower_and_upper_and_digits():
    gen = PasswordGenerator()
    pwd = gen.generate_password(use_lower=False, use_upper=False, use_digits=False)
    assert not any(c.islower() for c in pwd)
    assert not any(c.isupper() for c in pwd)
    assert not any(c.isdigit() for c in pwd)
  
def test_no_lower_and_upper_and_symbols():
    gen = PasswordGenerator()
    pwd = gen.generate_password(use_lower=False, use_upper=False, use_symbols=False)
    assert not any(c.islower() for c in pwd)
    assert not any(c.isupper() for c in pwd)
    assert not any(c in string.punctuation for c in pwd)
  
# test will fail if we test no lower, upper, digits and symbols
# as we will not be able to generate a password with all these options false

def test_strength():
    gen = PasswordGenerator()
    pwd = gen.generate_password(length=12)
    assert gen.check_strength(pwd)["score"] >= 3
    
def test_strength_no_digits():
    gen = PasswordGenerator()
    pwd = gen.generate_password(length=12, use_digits=False)
    assert gen.check_strength(pwd)["score"] >= 3
    
def test_strength_no_symbols():
    gen = PasswordGenerator()
    pwd = gen.generate_password(length=12, use_symbols=False)
    assert gen.check_strength(pwd)["score"] >= 3
    
def test_strength_no_lower():
    gen = PasswordGenerator()
    pwd = gen.generate_password(length=12, use_lower=False)
    assert gen.check_strength(pwd)["score"] >= 3
    
def test_strength_no_upper():
    gen = PasswordGenerator()
    pwd = gen.generate_password(length=12, use_upper=False)
    assert gen.check_strength(pwd)["score"] >= 3
    