import json
class PasswordStorage:
    
    def __init__(self, file_path):
        self.file_path = file_path
        
    def write_passwords(self, new_password):
      try: # trying to read existing password entries
        with open(self.file_path, 'r') as f:
          password = json.load(f)
          if isinstance(password, dict): # if the password is a dict, convert it to a list
            password = [password]
      except (FileNotFoundError, json.JSONDecodeError):
        # if the password doesn't exist or is empty, start with an empty list
        password = []
        
      password.append(new_password)
      
      with open(self.file_path, 'w', newline='') as f:
        json.dump(password, f, indent=2)
        
    
    # TODO: Read passwords from JSON file
    def read_passwords(self):
      with open (self.file_path) as f:
        data = json.load(f) # parses json into python dict/list
      return data
    
    
    
    
    
    