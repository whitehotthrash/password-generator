from password_storage import PasswordStorage
from password_generator import PasswordGenerator

def test_write_and_read_passwords():
    storage = PasswordStorage("test_passwords.json")
    test_data = [{"name": "test", "password": "abc123"}]
    storage.write_passwords(test_data)
    assert storage.read_passwords() == test_data
    
def test_read_empty_file():
    storage = PasswordStorage("empty_file.json")
    # Should return empty list if the file doesn't exist or is empty
    assert storage.read_passwords() == []
    
def test_write_multiple_passwords():
    storage = PasswordStorage("test_multiple.json")
    generator = PasswordGenerator() # call the actual generator for this unit test
    passwords = [
        {"name": "gmail", "password": generator.generate_password(length=8)},
        {"name": "facebook", "password": generator.generate_password(length=10)}
    ]
    storage.write_passwords(passwords)
    assert len(storage.read_passwords()) == 2
    
def test_file_creation():
    import os
    generator = PasswordGenerator()
    test_file = "new_file.json"
    storage = PasswordStorage(test_file)
    storage.write_passwords([{"name": "test", "password": generator.generate_password(length=12)}])
    assert os.path.exists(test_file)
    
def test_overwrite_password():
    generator = PasswordGenerator()
    test_file = "test_overwrite.json"
    storage = PasswordStorage(test_file)
    
    first_password = generator.generate_password(length=8)
    storage.write_passwords([{"name": "outlook", "password": first_password}])
    
    # Overwrite
    second_password = generator.generate_password(length=10)
    storage.write_passwords([{"name": "outlook", "password": second_password}])
    
    stored_passwords = storage.read_passwords()
    assert len(stored_passwords) == 1
    assert stored_passwords[0]["name"] == "gmail"
    assert stored_passwords[0]["password"] == second_password