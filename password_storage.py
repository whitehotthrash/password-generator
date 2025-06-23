import json
class PasswordStorage:
    
    def __init__(self, file_path):
        self.file_path = file_path
        
    def write_passwords(self, passwords):
      with open(self.file_path, 'w', newline='') as f:
        json.dump(passwords, f, indent=2)
        
    def read_passwords(self):
      try:
        with open (self.file_path) as f:
          data = json.load(f) # parses json into python dict/list
          if isinstance(data, dict): # if the password is a dict, convert it to a list
            data = [data]
          return data
      except (FileNotFoundError, json.JSONDecodeError):
        return []